#thư viện dictionary
if __name__ == "__main__":
    product={
        "iphone": "Apple iPhone 14 Pro Max",
        "samsung": "Samsung Galaxy S23 Ultra",
        "google": "Google Pixel 7 Pro",
        "xiaomi": "Xiaomi 13 Pro",
    }
    print(product)
    print(product["iphone"])
    print(product.get("samsung"))
    print(product.get("nokia", "Product not found"))  # Trả về giá trị mặc định nếu không tìm thấy
    if product.get("samsung"): # trả về true nếu có giá trị
        print("Samsung is available")
    else:
        print("Samsung is not available")
    # Thêm sản phẩm mới
    product["nokia"] = "Nokia 9 PureView"
    product.update({"oneplus": "OnePlus 11"}) # Thêm nhiều sản phẩm
    product.setdefault("huawei", "Huawei P50 Pro")  # Thêm nếu không tồn tại
    print(product)
    # Cập nhật sản phẩm
    product["google"] = "Google Pixel 7a"
    product.update({"sony": "Sony Xperia 1 IV"})
    print(product)
    # Xóa sản phẩm
    del product["xiaomi"]
    product.pop("iphone", None)  # Trả về None nếu không tìm thấy
    product.popitem()  # Xóa mục cuối cùng trong dictionary
    product.clear()  # Xóa tất cả các mục trong dictionary
    print(product)
    # in sản phẩm
    print("Product List:")
    for key, value in product.items():
        print(f"{key}: {value}")