# Weather map

## 概要

地図上で選択した地点の現在の天気を表示します

![スクリーンショット 2025-03-08 202029](https://github.com/user-attachments/assets/c2f86a70-9854-4cb6-857d-6aadd0c45d9e)

## 構成

- [Frontend](https://github.com/paquete-tab/Weather-map-frontend)
  - Cloudflare Pages
  - React
- Backend
  - Amazon EC2
  - Docker
  - Nginx
  - Python
  - Amazon RDS
  - OpenWeather
 
Frontend-Backend間の通信に、TypeScriptで実装しCloudflare Workers上で稼働させている[HTTPS Proxy](https://github.com/paquete-tab/HTTPS-Proxy)を使用しています

![構成図](https://github.com/user-attachments/assets/3690f8a9-8cde-4173-a3a3-58a8f4bb5bf1)

