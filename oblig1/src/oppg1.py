
# 1.1 Self join
import DBmanager as db

# Setup for On Stage Personell
osp_name = "OnStagePersonnel"
osp_attributes = (
     ("ospID", "integer"), 
     ("name", "text"),
     ("lastname", "text") 
)

# Setup for Stage Manager
sm_name = "StageManager"
sm_attributes = (
     ("ospID", "integer"),
     ("smID", "integer"),
     ("name", "text"),
     ("lastname", "text"),
     ("function", "text") 
)


if __name__ == "__main__":
    db_obj = db.DBmanager("oblig1.db")
    db_obj.create_table(osp_name, osp_attributes)
    db_obj.create_table(sm_name, sm_attributes)
    print(db.DBmanager.tables)

