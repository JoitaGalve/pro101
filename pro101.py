import dropbox

class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken

    def uploadFiles(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accessToken)
        f = open(fileFrom, 'rb')
        dbx.files_upload(f.read(), fileTo)

def main():
    accessToken = 'sl.BAHJb2VP8UhUDW6yMSsUm55brHRNmIMD5dwQUR4GN2JrWB4v4AttesWS4Yn39KGkojXlI8Vx-lUFoFm_KADqVG9f5QbW2Op7nT2OvbI5IkHe55gLwzwpfVJQ_vIA9bgH_pxBP9NPSJI3'
    transferData = TransferData(accessToken)
    fileFrom = input("Enter the full path to transfer: ")
    fileTo = input("Enter the full path to upload to dropbox: ")
    transferData.uploadFiles(fileFrom, fileTo)
    print("The file has been transfered")

main()