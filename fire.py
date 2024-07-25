# import firebase_admin
# from firebase_admin import firestore

# # Application Default credentials are automatically created.
# app = firebase_admin.initialize_app()
# db = firestore.client()

import firebase_admin
from firebase_admin import credentials, firestore

# 서비스 계정 키 파일 경로
cred = credentials.Certificate('path/to/serviceAccountKey.json')

# Firebase Admin SDK 초기화
firebase_admin.initialize_app(cred)

# Firestore 클라이언트 초기화
db = firestore.client()

# 데이터 추가
doc_ref = db.collection('users').document('alovelace')
doc_ref.set({
    'first': 'Ada',
    'last': 'Lovelace',
    'born': 1815
})

# 데이터 읽기
doc = doc_ref.get()
if doc.exists:
    print(f'Document data: {doc.to_dict()}')
else:
    print('No such document!')

# 데이터 업데이트
doc_ref.update({
    'born': 1816
})

# 데이터 삭제
# doc_ref.delete()
