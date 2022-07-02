import gspread
from oauth2client.service_account import ServiceAccountCredentials
from list_handler import format_emtpy_strings


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds =ServiceAccountCredentials.from_json_keyfile_name("H:\WorkspacePython\SheetsApiTest\service_account.json", scope)
client = gspread.authorize(creds)


def list_getter(pvm_lt, hybrid_lt, pvp_lt):
        
        sh = client.open("testTable").worksheet("Main Tabelle")
        max_rows = len(sh.get_all_values())
        notationRange = 'A2:D'+str((max_rows-4))

        member_list = sh.get_values(notationRange)
        member_list.sort()
        member_list_f = format_emtpy_strings(member_list)

        counter=-1
        for member in member_list_f:
                counter+=1
                for reaction in pvm_lt:
                        if member[0]==reaction:
                                pvm=member[1]+1
                                hybrid=member[2]
                                pvp=member[3]
                                e=member[0],pvm,hybrid,pvp
                                member_list_f.pop(counter)
                                member_list_f.insert(counter, e)  
        
        counter=-1
        for member in member_list_f:
                counter+=1
                for reaction in hybrid_lt:
                        if member[0]==reaction:
                                pvm=member[1]
                                hybrid=member[2]+1
                                pvp=member[3]
                                e=member[0],pvm,hybrid,pvp
                                member_list_f.pop(counter)
                                member_list_f.insert(counter, e)          
                                
        counter=-1
        for member in member_list_f:
                counter+=1
                for reaction in pvp_lt:
                        if member[0]==reaction:
                                pvm=member[1]
                                hybrid=member[2]
                                pvp=member[3]+1
                                e=member[0],pvm,hybrid,pvp
                                member_list_f.pop(counter)
                                member_list_f.insert(counter, e)                                           
        # print(member_list_f)
        
        sh.update (notationRange, member_list_f)
        
