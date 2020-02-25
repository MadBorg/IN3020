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
     {"table": "OnStagePersonnel", "key": "ospID","forign_key": "ospID"},
)

sm_primary_key = ( # TODO : test
     "ospID", "smID"
)

path_to_names_csv = "https://raw.githubusercontent.com/hadley/data-baby-names/master/baby-names.csv"
names_df = pd.read_csv(path_to_names_csv, sep=',')


name_counter = 0
# Data for osp
osp_N = 100
osp_data = [
     # {ospID: <int>, name: <str>, lastname: <str>}
]

firsname_data_osp = names_df["name"][name_counter:name_counter + osp_N].to_list()æ; name_counter += osp_N
lastname_data_osp = names_df["name"][name_counter:name_counter + osp_N].to_list()æ; name_counter += osp_N
start_id = 1000

ospID = start_id
for firstname, lastname in zip(firsname_data_osp, lastname_data_osp):
     osp_data.append(
          {"ospID": ospID, "name": firstname, "lastname": lastname}
     )
     ospID += 1

# Data for sm
sm_N = 20
sm_data = [
     # {ospID: <int>, smID: <int>, name: <str>, lastname: <str>, function: <str>}
]

# ip.embed()
firsname_data_sm = names_df["name"][name_counter:name_counter + osp_N].to_list()æ; name_counter += sm_N
lastname_data_sm = names_df["name"][name_counter:name_counter + osp_N].to_list()æ; name_counter += sm_N
functions = ("rehearsals", "coordinating", "communicating", "overseeing", "calling cues")
smIDs = np.random.randint(100, 1000, size=osp_N)
function_indices = np.random.randint(0, len(functions), size=osp_N)

# Assigning sm to all osp
for i in range(osp_N):
     sm_data.append({
          "ospID": osp_data[i]["ospID"],
          "smID": smIDs[i],
          "name": firsname_data_sm[i],
          "lastname": lastname_data_sm[i],
          "function": functions[ function_indices[i] ]
          })



if __name__ == "__main__":
     path = ":memory:"
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

     # # Test last insert
     # db_obj.check_specific_insert(
     #      osp_name, osp_data
     # )

     # Query for task
     


     # print(db.DBM.tables)
     db_obj.close()
