# -*- coding: utf-8 -*-
from pymongo import MongoClient
import pprint
import datetime

# MongoDB 외부접속을 가능하게 하려면
# 설정파일애 'bind_ip=아이피주소' 를 추가

# 몽고디비 연결객체 만들기
# client = MongoClient()
try:
    # client = MongoClient('192.168.56.101', 27017)
    client = MongoClient('mongodb://192.168.56.101:27017')
except Exception as ex:
    print(ex)

# 데이터베이스 객체 사져오기
# db = client['zzyzzy']
db = client.zzyzzy

# 컬렉션 객체 가져오기
coll = db['inventory']
coll2 = db.inventory2
coll3 = db.restaurants

# 단일문서 조회
# print(coll.find_one())

# 단일문서 조회 - JSON을 보기좋게 출력하기 (pprint)
# pprint.pprint(coll.find_one())

# 전체문서 조회
# pprint.pprint(coll.find())
# cursor = coll.find()
# for doc in cursor:
#     pprint.pprint(doc)

# cursor = coll2.find()
# for doc in cursor:
#     pprint.pprint(doc)

# cursor = coll3.find()
# for doc in cursor:
#     pprint.pprint(doc)

# 조건으로 질의하기
# cursor = coll.find({ 'item':'notebook' })
# for doc in cursor:
#     print(doc)

# qty가 50보다 작은 item 조회
# cursor = coll2.find({ 'qty': { "$lte" : 50 } })
# for doc in cursor:
#     print(doc)

# 우편번호가 10075인 음식점 조회
# cursor = coll3.find({ 'zipcode.address': '10462' })
# for doc in cursor:
#     print(doc)

# 데이터 추가하기 - JSON 생성
# students = { 'hakbun': "a12345",
#             'name': "혜교",
#             'addr': "seoul, korea",
#             'regdate': datetime.datetime.now() }

# 데이터 추가학고 생성된 object_id 값을 objId 변수에 저장
# objId = db.students.insert_one(students).inserted_id

# print(objId)
# print(db.students.find_one())

# 데이터 추가하기 - 여러개 생성
# many_students = [{ 'hakbun': "a12345",
#                   'name': "혜교",
#                   'addr': "seoul, korea",
#                   'regdate': datetime.datetime.now() },
#                 { 'hakbun': "x24680",
#                   'name': "수지",
#                   'addr': "daejeon, korea",
#                   'regdate': datetime.datetime.now() }]

# result = db.students.insert_many( many_students )
# print(result.inserted_ids)

# 데이터 수정
# 학번 a12345인 학생의 주소를 인천으로 변경
result = db.student.update_one({ 'hakbun': "a12345" },
                               { "$set": { 'addr': "incheon, korea" } })

print(result.matched_count, result.modified_count)


# result = db.student.update_many({ 'hakbun': "a12345" },
#                                { "$set": { 'addr': "incheon, korea" } })
#
# print(result.matched_count, result.modified_count)
#
# # 데이터 삭제
# # 학번 a12345인 학생 정보 삭제
# result = db.student.delete_one({ 'hakbun': "a12345" })
# print(result.deleted_count)
#
# result = db.student.delete_many({ 'hakbun': "a12345" })
# print(result.deleted_count)
#
# result = db.student.delete_many({}) # 모두 삭제
# print(result.deleted_count)
#
# 몽고디비 접속해제
client.close()
