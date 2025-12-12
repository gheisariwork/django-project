# ۱ ساخت ایمیج (فقط یک بار)
docker build -t mydjango .

# ۲ اجرای دیتابیس (postgres)
docker run -d \
  --name postgres-db \
  -e POSTGRES_DB=bookstore \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=pass123 \
  -p 5432:5432 \
  postgres:15-alpine

# ۳ اجرای پروژه جنگو و وصل کردن به دیتابیس
docker run -d --name mydjango-app \
  -p 8000:8000 \
  --link postgres-db \
  -e DATABASE_URL=postgres://user:pass123@postgres-db:5432/bookstore \
  mydjango
