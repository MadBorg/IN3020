import math
import IPython as ip

class CostCalc:

    def __init__(self, rel, M):
        """
        Input:
        ---------
        R, S: relation
            Relations to do operations on
        """
        self.R = rel[0]
        if len(rel) == 2:
            self.S = rel[1]
        self.M = M
        

    # - Operations
    def projection(self, new_S):
        """
        calc new relation, assumed
        """
        new_T = self.R.T
        new_V = self.R.V
        new_S = new_S
        new_rel = relation(
            new_T, new_V, new_S, block_size=self.R.block_size, column_names=self.R.columns
        )
        return new_rel

    def selection(self, new_T):
        """
        calc new relation, assumed
        """
        new_T = new_T
        new_V = new_T
        new_S = self.R.S
        new_rel = relation(
            new_T, new_V, new_S, block_size=self.R.block_size, column_names=self.R.columns
        )
        return new_rel


    def natural_join(self): 
        """
        calc new relation, asumed (assuming all distinct from the samllest is the join amount)
        """
        R, S = self.R, self.S
        new_T = min((R.V, S.V))
        new_V = new_T
        new_S = R.S + S.S
        if R.columns and S.columns:
            new_cols = R.columns + S.columns
        else:
            new_cols = None
        new_rel = relation(
            new_T, new_V, new_S, block_size=min((R.block_size, R.block_size)),  column_names=new_cols
        )
        return new_rel


    # - Operation methods
    # natural Join
    def natural_join_one_pass(self):
        R, S = self.R, self.S
        mem = 1 + S.B
        discIO = R.B + S.B
        return {"mem": mem, "discIO": discIO}

    def natural_join_block_based_nested_loop(self):
        R, S, M = self.R, self.S, self.M
        mem = 2
        discIO = S.B + R.B * math.ceil(S.B / (M-1))
        return {"mem": mem, "discIO": discIO}

    def natural_join_simple_two_pass_sorting(self):
        R, S = self.R, self.S
        mem = math.sqrt(S.B)
        discIO = 5*R.B + 5*S.B
        return {"mem": mem, "discIO": discIO}

    def natural_join_sort_join(self):
        R, S = self.R, self.S
        mem = math.sqrt(R.B + S.B)
        discIO = 3*R.B + 3*S.B
        return {"mem": mem, "discIO": discIO}

    def natural_join_hash_join(self):
        R, S = self.R, self.S
        mem = math.sqrt(S.B)
        discIO = 3*R.B + 3*S.B
        return {"mem": mem, "discIO": discIO}

    def natural_join_hybrid_hash_join(self):
        R, S, M = self.R, self.S, self.M
        mem = math.sqrt(S.B)
        discIO = (3 - 2*M/S.B) * (R.B + S.B)
        return {"mem": mem, "discIO": discIO}

    def natural_join_cluster_index_on_sy(self):
        R, S = self.R, self.S
        mem = 2
        discIO = R.T * math.ceil(S.B/S.V) # might be wrong, compare with: https://www.uio.no/studier/emner/matnat/ifi/IN3020/v20/Lectures/071---effective-query-execution-part-1.pdf
        return {"mem": mem, "discIO": discIO}

    def natural_join_cluster_index_on_sy_s_not_sorted_on_y(self):
        R, S = self.R, self.S
        mem = 2
        discIO = R.T * S.T / S.V
        return {"mem": mem, "discIO": discIO}

    def natural_join_zig_zag_index_join_on_A(self):
        raise NotImplementedError()
        # R, S = self.R, self.S
        # mem = 
        # discIO = R.B + S.B
        # return {"mem": mem, "discIO": discIO}

    # selection
    def selection_in_mem(self):
        R = self.R
        mem = 1
        discIO = 0
        return {"mem": mem, "discIO": discIO}
    def selection_no_index(self):
        R = self.R
        mem = 1
        discIO =  R.B
        return {"mem": mem, "discIO": discIO}
    def selection_cluster_index(self):
        R = self.R
        mem = 1
        discIO = math.ceil( R.B / R.V ) # might be wrong
        return {"mem": mem, "discIO": discIO}
    
    # projection
    def projection_in_mem(self):
        R = self.R
        mem = 1
        discIO = 0
        return {"mem": mem, "discIO": discIO}
    def projection_no_index(self):
        R = self.R
        mem = 1
        discIO =  R.B
        return {"mem": mem, "discIO": discIO}
    def projection_cluster_index(self):
        R = self.R
        mem = 1
        discIO = math.ceil( R.B / R.V ) # might be wrong
        return {"mem": mem, "discIO": discIO}



class relation:
    def __init__(self, T, V, S, block_size=10, column_names=None):
        """
        Input:
        ---------
        T: int
            indicates the number of tuples in a relation
        V: dict
            number of distinct tuples for attribute V[<attr>]
        S: int
            size of a tuple in R bytes
        Block_size: int
            Size of the blocks in the b-tree
        column_names: iterable<string>
            names for the cols int the relation
        """
        # Asserts
        # TODO : Check datatypes
        # Assignments
        self.columns = column_names

        self._T = T
        self._V = V
        self._S = S
        self.block_size = block_size

    @property
    def T(self):
        return self._T

    @property
    def V(self):
        return self._V

    @property
    def S(self):
        return self._S

    @property
    def B(self):
        # ip.embed()
        records_per_block = math.ceil( self.block_size/ self.S )
        b_size = math.ceil( self.T / records_per_block )

        # print(f"Records pr. block: {records_per_block}")
        return b_size

def natural_join_print(cost_obj, name = None):
    if name:
        print(f"\n__Memory and cost for natural join on {name}__")
    else:
        print("\n__Memory and cost for natural join__")
    print(f"One pass:\n" +\
        f"   {cost_obj.natural_join_one_pass()}")
    print(f"Block based nested loop:\n" +\
        f"   {cost_obj.natural_join_block_based_nested_loop()}")
    print(f"Simple two pass sorting:\n" +\
        f"   {cost_obj.natural_join_simple_two_pass_sorting()}")
    print(f"Sort join:\n" +\
        f"   {cost_obj.natural_join_sort_join()}")
    print(f"Hash join:\n" +\
        f"   {cost_obj.natural_join_hash_join()}")
    print(f"Hybrid hash join:\n" +\
        f"   {cost_obj.natural_join_hybrid_hash_join()}")
    print(f"(cluster) Index join on A:\n" +\
        f"   {cost_obj.natural_join_cluster_index_on_sy()}")
    print(f"(cluster not sorted on y) Index join on A:\n" +\
        f"   {cost_obj.natural_join_cluster_index_on_sy_s_not_sorted_on_y()}")

def selection_print(cost_obj, name=None):
    if name:
            print(f"\n__Memory and cost for selection on {name}__")
    else:
        print("\n__Memory and cost for selection__")
    print(f"In mem:\n" +\
        f"   {cost_obj.selection_in_mem()}")
    print(f"No index:\n" +\
        f"   {cost_obj.selection_no_index()}")
    print(f"Cluster index:\n" +\
        f"   {cost_obj.selection_cluster_index()}")

def projection_print(cost_obj, name=None):
    if name:
            print(f"\n__Memory and cost for projection on {name}__")
    else:
        print("\n__Memory and cost for projection__")
    print(f"In mem:\n" +\
        f"   {cost_obj.projection_in_mem()}")
    print(f"No index:\n" +\
        f"   {cost_obj.projection_no_index()}")
    print(f"Cluster index:\n" +\
        f"   {cost_obj.projection_cluster_index()}")

if __name__ == "__main__":
    # init
    number_of_good_movies = 500 # arbitrary selected number, since it was not specified
    size_of_name = size_of_teamName = 40
    size_of_movie = 80
    size_of_rating = 4
    M = 101
    block_size_in_B = 4 * 1e3
    FXTeamsInMovies = relation(
        T=10_000, V=1_500, S=140, block_size=block_size_in_B, column_names=None
    )
    FXTeam = relation(
        T=1_500, V=1_500, S=80, block_size=block_size_in_B, column_names=None
    )


    # Method one
    cost_film_rel = CostCalc(rel=(FXTeam, FXTeamsInMovies), M=M)
    natural_join_print(cost_film_rel)

    joined = cost_film_rel.natural_join()
    cost_joined = CostCalc([joined], M)
    selection_print(cost_joined)

    selected = cost_joined.selection(new_T=number_of_good_movies) 
    cost_selected = CostCalc([selected], M)
    projection_print(cost_selected)

    projected = cost_selected.projection(new_S = size_of_movie + size_of_name) # name is 40 bytes and movie is 80 bytes
    
    # Pushed down method
    print("\n__Pushed down Method__")

    # Projection on FXTeamsInMovies
    cost_FXTeamsInMovies = CostCalc(rel=[FXTeamsInMovies], M=M)
    projection_print(cost_FXTeamsInMovies, name="cost_FXTeamsInMovies")
    projected_FXTeamInMovies = cost_FXTeamsInMovies.projection(new_S = size_of_movie + size_of_teamName)
    # cost_projected_FXTeamInMoVies = CostCalc(rel=[projected_FXTeamsInMoVies], M=M)
    
    # Selection on FXTeam
    cost_FXTeam = CostCalc(rel=[FXTeam], M=M)
    selection_print(cost_FXTeam, name="cost_FXTeam")
    selected_FXTeam = cost_FXTeam.selection(new_T = number_of_good_movies)

    # Projection on FXTeam
    cost_FXTeam = CostCalc(rel=[selected_FXTeam], M=M)
    projection_print(cost_FXTeam, name = "FXTeam")
    projected_FXTeam = cost_FXTeam.projection(new_S = size_of_name + size_of_rating)
    # cost_projected_FXTeam =CostCalc(rel[projected_FXTeam], M=M)

    # Natural join
    cost_joined = CostCalc(rel=[projected_FXTeam, projected_FXTeamInMovies], M=M)
    natural_join_print(cost_joined, name="cost_joined")
    joined = cost_joined.natural_join()

    # Final projection
    cost_projected = CostCalc(rel=[joined], M=M)
    projection_print(cost_projected, name=" final cost_projected" )









