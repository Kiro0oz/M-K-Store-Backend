# E-Commerce API

A complete E-commerce backend API built with **Django Rest Framework (DRF)** providing features like user authentication, product management, cart handling, order processing, and reviews.

## 🚀 Features
- User authentication (Registration, Login, Logout)
- Product listing, details, and image support
- Cart management (Add, Remove, View, Clear Cart)
- Order processing (Create, Retrieve, Delete, Process)
- User reviews & ratings on products

## 📌 Tech Stack
- **Backend:** Django, Django REST Framework (DRF)
- **Database:** PostgreSQL / SQLite
- **Authentication:** Token-based authentication

---

## 🛠️ Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/ecommerce-api.git
   cd ecommerce-api
   ```

2. **Create a Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   ```sh
   python manage.py migrate
   ```

5. **Create Superuser**
   ```sh
   python manage.py createsuperuser
   ```

6. **Run Development Server**
   ```sh
   python manage.py runserver
   ```
   The API will be available at: `http://127.0.0.1:8000/`

---

## 🔑 Authentication
### 1️⃣ Register a New User
**Endpoint:** `POST /api/auth/register/`

**Request Body:**
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```
**Response:**
```json
{
  "message": "User registered successfully"
}
```

### 2️⃣ Login
**Endpoint:** `POST /api/auth/login/`

**Request Body:**
```json
{
  "username": "john_doe",
  "password": "securepassword123"
}
```
**Response:**
```json
{
  "token": "your-auth-token"
}
```

---

## 🛒 Cart Management
### 1️⃣ Add to Cart
**Endpoint:** `POST /api/cart/add/`

**Request Body:**
```json
{
  "userId": 1,
  "products": [
    { "productId": 3, "quantity": 2 }
  ]
}
```
**Response:**
```json
{
  "message": "Products added to cart successfully"
}
```

### 2️⃣ View Cart
**Endpoint:** `GET /api/cart/view/`

**Response:**
```json
{
  "id": 1,
  "user": 1,
  "items": [
    {
      "id": 5,
      "product": { "id": 3, "title": "Product Name", "price": 20.5, "image": "http://..." },
      "quantity": 2,
      "subtotal": 41.0
    }
  ],
  "total_price": 41.0
}
```

### 3️⃣ Clear Cart
**Endpoint:** `DELETE /api/cart/clear/`

**Response:**
```json
{
  "message": "Cart cleared successfully"
}
```

---

## 📦 Order Management
### 1️⃣ Place a New Order
**Endpoint:** `POST /api/order/new/`

**Request Body:**
```json
{
  "order_Items": [
    { "product": 3, "quantity": 2, "price": 20.5 }
  ],
  "city": "New York",
  "zip_code": "10001",
  "street": "5th Avenue",
  "phone_no": "123456789",
  "country": "USA"
}
```
**Response:**
```json
{
  "id": 1,
  "total_amount": 41.0,
  "status": "Processing"
}
```

### 2️⃣ Get Order Details
**Endpoint:** `GET /api/order/get/{order_id}/`

### 3️⃣ Process Order (Admin Only)
**Endpoint:** `PUT /api/order/process/{order_id}/`

### 4️⃣ Delete Order
**Endpoint:** `DELETE /api/order/delete/{order_id}/`

---

## ⭐ Reviews
### 1️⃣ Add a Review
**Endpoint:** `POST /api/review/add/{product_id}/`

**Request Body:**
```json
{
  "rating": 5,
  "comment": "Great product!"
}
```
**Response:**
```json
{
  "message": "Comment Added Successfully"
}
```

### 2️⃣ Get Product Reviews
**Endpoint:** `GET /api/review/{product_id}/`

---

## 📄 API Documentation
For complete API documentation, visit: [API Docs](https://www.apidog.com/apidoc/shared-fe2d22aa-5402-4def-8782-14b8729cfbd2)

---

## 🏗️ Contributing
1. Fork the repository.
2. Create a new feature branch.
3. Make your changes and commit.
4. Push your changes and create a pull request.

---

## 🛡️ License
This project is licensed under the MIT License.



