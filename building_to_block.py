import arcpy

env = r"E:/VUB/Master_Thesis/Brussels/BrusselsData/Mingyue_Data.gdb/Mingyue_Data.gdb"
arcpy.env.workspace = env
arcpy.env.overwriteOutput = True

building=r"binb_asd"
#building=arcpy.Sort_management(sj, "binb_asd", [["ID", "ASCENDING"]])


block=r"UrbAdm_BLOCK"

field_building=['ID','Tree_85','PGS_300']
field_block=['ID','Tree_pct','Park_pct']

count_tree=0
count_park=0
n=0
lastid=4002938

with arcpy.da.SearchCursor(building,field_building) as cursor:
    for row in cursor:        
        id1=row[0]
        tree=row[1]
        park=row[2]
        
        if tree==None:
            tree=0
        if park==None:
            park=0
        
        print('Building in block: ',id1,'3 trees view: ',tree,'300 meters to park: ',park)
        if id1!=lastid:
            with arcpy.da.UpdateCursor(block,field_block) as cursor2:
                for i in cursor2:
                    if i[0]==lastid:
                        print("number of buildings meet 3: ",count_tree,"number of buildings meet 300: ",count_park,"number of buildings in the block: ",n)
                        tree_pct=count_tree/n
                        park_pct=count_park/n
                        i[1]=tree_pct
                        i[2]=park_pct
                        cursor2.updateRow(i)
            del cursor2
            n=0
            count_tree=0
            count_park=0
                        
        if tree>1 or tree==1:
            count_tree+=1
        if park>1 or park==1:
            count_park+=1
        n+=1
        lastid=id1
        


        
