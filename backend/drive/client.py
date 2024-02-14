from googleapiclient.discovery import build
from google.oauth2 import service_account
import os
from dotenv import load_dotenv
from googleapiclient.http import MediaFileUpload
    
#Carrega as variáveis de ambiente do arquivo .env
load_dotenv(dotenv_path=".env.prod")

class DriveClient:
    def __init__(self):
        self.local = os.chdir("./backend/drive")
        self.SCOPES = ['https://www.googleapis.com/auth/drive']
        self.SERVICE_ACCOUNT_FILE = 'service_account.json'
        self.creds = self.authenticate()
        self.PARENT_FOLDER_ID = os.getenv("URL_PATH")
        self.service = build('drive', 'v3', credentials=self.creds)
        self.localparquet = "../drive/dataapi/"

    def authenticate(self):
        creds = service_account.Credentials.from_service_account_file(self.SERVICE_ACCOUNT_FILE, scopes = self.SCOPES)
        return creds

    def upload_dataset(self):
        try:
            creds = self.authenticate()

            for arquivo in os.listdir(self.localparquet):
                if arquivo.endswith(".parquet"):
                    caminho_arquivo = os.path.join(self.localparquet, arquivo)

                    file_metadata = {
                        'name': arquivo,
                        'parents': [self.PARENT_FOLDER_ID]
                    }

                    # Configurar corpo da mídia para upload binário
                    media_body = MediaFileUpload(caminho_arquivo, mimetype='application/octet-stream', resumable=True)

                    file = self.service.files().create(
                        body=file_metadata,
                        media_body=media_body
                    ).execute()

                    print(f"Upload do arquivo {arquivo} realizado com sucesso.")
                else:
                    print("Arquivo não esta no formato parquet")

        except Exception as e:
            print(e)
            print("Por favor revise o local ou nome do arquivo. Arquivo não encontrado")


if __name__ == "__main__":
    DriveClient().upload_dataset()
