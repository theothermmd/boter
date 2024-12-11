import requests
bearer_token : str = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL21vdmllcGl4LmlyIiwiaWF0IjoxNzMzNzQzMDQ2LCJuYmYiOjE3MzM3NDMwNDYsImV4cCI6MTczNjMzNTA0NiwiZGF0YSI6eyJ1c2VyIjp7ImlkIjoiMyJ9fX0.3nhDfqRZ7BbdCg7cCcO1j_uBvR4LcO3j5LqEswO5gX0"
headers = { "Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json" }
# اطلاعات احراز هویت
BASE_URL = "https://moviepix.ir/wp-json/wp/v2"
USERNAME = "your_username"
PASSWORD = "your_password"


def get_trash_posts(page=1, per_page=50):
    url = f"{BASE_URL}/posts?status=trash&per_page={per_page}&page={page}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching posts:", response.text)
        return []

def delete_post(post_id):
    url = f"{BASE_URL}/posts/{post_id}?force=true"
    response = requests.delete(url, headers=headers)
    if response.status_code == 200:
        print(f"Deleted post ID: {post_id}")
    else:
        print(f"Error deleting post ID {post_id}:", response.text)

# حذف گروهی
page = 1
while True:
    posts = get_trash_posts(page=page)
    if not posts:  # اگر لیستی نبود
        break
    for post in posts:
        delete_post(post['id'])
    page += 1
