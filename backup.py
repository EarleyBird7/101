import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token=access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f=open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token='sl.A-aE1TPm06IrQpgIWePiJvcGxCrNFzzzRoKJB9Q6FNULbEjbmV56XL71-Jx-VTJJKfcuAVCKD19hKn-c2EL5IFnjlR7UTGh4dUG3LYQLOFHp1S8oUARzisHe5rkbxnzWNeu2m5E'
    transferData=TransferData(access_token)

    file_from = "text1.txt"
    file_to="/Class_Project/text2.txt"

    transferData.upload_file(file_from, file_to)
    print("file was moved :D")