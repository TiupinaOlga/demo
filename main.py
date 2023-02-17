import requests

class YaUploader:
  def __init__(self, _token: str):
    self.token = _token

  def upload(self, file_path: str):
    # """Метод загружает файл file_path на Яндекс.Диск"""
    upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    filename = file_path.split('/', )[-1]  #Получаем имя файла из пути
    # print(filename)
    headers = {'Content-type': 'application/json', 'Authorization': self.token} #Создаем заголовки
    # print(headers)
    params = {'path': filename} #Создаем параметры
    # print(params)
    res = requests.get(upload_url,headers=headers,params=params) #Делаем запрос
    # print(res.json())
    try:
      res.raise_for_status()
    except Exception as e:
      return('Ошибка при загрузке файла: ' + str(e))#Проверяем запрос, если он не валидный то выкинем исключение
    href_= res.json().get("href", "") #Получаем ссылку
    # print(href_)
    res = requests.put(href_, data = open(filename, "rb")) #Помещаем файл на яндекс диск
    res.raise_for_status() #Проверяем запрос, если он не валидный то выкинем исключение
    return "Файл успешно загружен"



if __name__ == '__main__':
  path_to_file = 'text.txt'
  token = 'y0_AgAAAAATyN3PAADLWwAAAADalLv5SmLMDPA1T3imDXdMLgVfDQInee8'
  uploader = YaUploader(token)
  result = uploader.upload(path_to_file)
  print(result)

