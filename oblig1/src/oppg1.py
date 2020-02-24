
# 1.1 Self join
import dbm as db

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
     {"name": "smID", "datatype": "INTEGER", "primary_key": True},
     {"name": "name", "datatype": "TEXT"},
     {"name": "lastname", "datatype": "TEXT"},
     {"name": "function", "datatype": "TEXT"} 
)
sm_references = (
     # table, key, forign_key, on delete, on update
     {"table": "OnStagePersonnel", "key": "ospID","forign_key": "ospID"},
)


# Data for osp


if __name__ == "__main__":
     path = ":memory:"
     db_obj = db.DBM(path)
     db_obj.create_table(
          name=osp_name, attributes=osp_attributes
     )
     db_obj.create_table(
          name=sm_name, attributes=sm_attributes, references=sm_references
     )
     # print(db.DBM.tables)

