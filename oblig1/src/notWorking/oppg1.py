import dbm as db
import pandas as pd
import numpy as np

import IPython as ip
# 1.1 Self join

# Setup for On Stage Personell
osp_name = "OnStagePersonnel"
osp_attributes = (
      # name, datatype, null, primary key, default
     {"name": "ospID", "datatype": "INTEGER", "primary_key": True}, 
     {"name": "name", "datatype": "TEXT"},
     {"name": "lastname", "datatype": "TEXT"}
)

# Setup for Stage Manager
sm_name = "StageManager"
sm_attributes = (
     # name, datatype, null, primary key, default
     {"name": "ospID", "datatype": "INTEGER"},
     {"name": "smID", "datatype": "INTEGER"},
     {"name": "name", "datatype": "TEXT"},
     {"name": "lastname", "datatype": "TEXT"},
     {"name": "function", "datatype": "TEXT"} 
)
sm_references = (
     # table, key, forign_key, on delete, on update
     {"table": osp_name, "key": "ospID","forign_key": "ospID"},
)

sm_primary_key = ( # TODO : test
     "ospID", "smID"
)

path_to_names_csv = "https://raw.githubusercontent.com/hadley/data-baby-names/master/baby-names.csv"
names_df = pd.read_csv(path_to_names_csv, sep=',')


name_counter = 0
# Data for osp
osp_N = 10
osp_data = [
     # {ospID: <int>, name: <str>, lastname: <str>}
]

firsname_data_osp = names_df["name"][name_counter:name_counter + osp_N].to_list(); name_counter += osp_N
lastname_data_osp = names_df["name"][name_counter:name_counter + osp_N].to_list(); name_counter += osp_N
start_id_osp = 1000

ospID = start_id_osp
for firstname, lastname in zip(firsname_data_osp, lastname_data_osp):
     osp_data.append(
          {"ospID": ospID, "name": firstname, "lastname": lastname}
     )
     ospID += 1

# Data for sm
sm_N = 3
sm_data = [
     # {ospID: <int>, smID: <int>, name: <str>, lastname: <str>, function: <str>}
]

# ip.embed()
firsname_data_sm = names_df["name"][name_counter:name_counter + osp_N].to_list(); name_counter += sm_N
lastname_data_sm = names_df["name"][name_counter:name_counter + osp_N].to_list(); name_counter += sm_N
functions = ("rehearsals", "coordinating", "communicating", "overseeing", "calling cues")
smIDs = np.random.randint(100, 1000, size=sm_N)
function_indices = np.random.randint(0, len(functions), size=osp_N)
sm_for_osp =np.random.randint(0, sm_N, size=osp_N)

# Making sm's
sms = [
     # {smID: <int>, name: <str>, lastname: <str>, function: <str>}
]
for i in range(sm_N):
     sms.append({
          "smID": smIDs[i],
          "name": firsname_data_sm[i],
          "lastname": lastname_data_sm[i],
          "function": functions[function_indices[i]]
     })

sm_data = [
     # {ospID: <int>, smID: <int>, name: <str>, lastname: <str>, function: <str>}
]

# Assigning sm to all osp
for i in range(osp_N):
     tmp_sm = sms[sm_for_osp[i]]
     sm_data.append({
          "ospID": start_id_osp + i,
          "smID": tmp_sm['smID'],
          "name": tmp_sm["name"],
          "lastname": tmp_sm["lastname"],
          "function": tmp_sm["function"]
     })
     print(f'tmp_sm smID: {tmp_sm["smID"]} ')




if __name__ == "__main__":
     # path = ":memory:"
     path  = "oblig1\\db\\oblig.db"
     db_obj = db.DBM(path)
     db_obj.create_table(
          name=osp_name, attributes=osp_attributes
     )
     db_obj.create_table(
          name=sm_name, attributes=sm_attributes, references=sm_references
     )

     # Inserting data
     #   Osp
     db_obj.insert(osp_name, osp_data)
     #   sm
     db_obj.insert(sm_name, sm_data)

     # All from osp
     q = """
     SELECT * FROM OnStagePersonnel
     """
     r = db_obj.query(q)
     print(f"ALL FROM OSP: \n{r.fetchall()}\n")

     # All from sm
     q = """
     SELECT * FROM StageManager
     """
     r = db_obj.query(q)
     print(f"ALL FROM sm: \n{r.fetchall()}\n")


     # # Test last insert
     # db_obj.check_specific_insert(
     #      osp_name, osp_data
     # )

     # Query for task
     q = """
     SELECT personel.ospID, manager.smID, manager.function
     -- SELECT personel.name, personel.lastname, manager.name, manager.lastname, manager.function
     FROM OnStagePersonnel personel
     LEFT JOIN StageManager manager
          WHERE personel.ospID == manager.ospID

     GROUP BY manager.function
     """
     r = db_obj.query(q)
     res = r.fetchall()
     print(res)


     print(db.DBM.tables)
     db_obj.close()
