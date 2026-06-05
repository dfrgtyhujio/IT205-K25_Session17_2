product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5"
]


def print_product_labels():
    print("\n--- DANH SÁCH TEM NHÃN ---")
    
    if len(product_list) == 0:
        print("Danh sách sản phẩm trống.")
        return

    for item in product_list:
        parts = item.split("-")
        
        if len(parts) < 4:
            print("Bỏ qua sản phẩm do sai cấu trúc dữ liệu.")
            continue
            
        sp_id = parts[0]
        sp_name = parts[1]
        sp_price_str = parts[2]
        sp_rating_str = parts[3]
        
        if not sp_price_str.isdigit():
            print(f"Bỏ qua sản phẩm {sp_id} do giá tiền không hợp lệ.")
            continue
            
        price_num = int(sp_price_str)
        formatted_price = f"{price_num:,} VND"
        
        data_dict = {
            "id": f"{sp_id:<10}",
            "name": sp_name,
            "price": formatted_price,
            "rating": sp_rating_str
        }
        
        template = "Mã: {id} | Tên: {name:<20} | Giá: {price:<16} | Rating: {rating}*"
        print(template.format_map(data_dict))


def sort_products():
    print("\n--- SẮP XẾP SẢN PHẨM ---")
    
    if len(product_list) == 0:
        print("Danh sách sản phẩm trống, không thể sắp xếp.")
        return

    n = len(product_list)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            
            parts_i = product_list[i].split("-")
            rating_i = float(parts_i[3])
            price_i = int(parts_i[2])
            
            parts_j = product_list[j].split("-")
            rating_j = float(parts_j[3])
            price_j = int(parts_j[2])
            
            if rating_i < rating_j:
                temp = product_list[i]
                product_list[i] = product_list[j]
                product_list[j] = temp

            elif rating_i == rating_j:
                if price_i > price_j:
                    temp = product_list[i]
                    product_list[i] = product_list[j]
                    product_list[j] = temp

    print("Đã sắp xếp thành công! Cập nhật danh sách:")
    count = 1
    for item in product_list:
        print(f"{count}. {item}")
        count = count + 1


def calculate_total_value():
    print("\n--- TỔNG GIÁ TRỊ KHO ---")
    
    if len(product_list) == 0:
        print("Tổng giá trị các mặt hàng hiện tại là: 0 VND.")
        return
        
    total_value = 0
    has_valid_price = False
    
    for item in product_list:
        parts = item.split("-")
        if len(parts) >= 3:
            price_str = parts[2]
            if price_str.isdigit():
                total_value = total_value + int(price_str)
                has_valid_price = True
            else:
                clean_price = ""
                for char in price_str:
                    if char.isdigit():
                        clean_price = clean_price + char
                if clean_price != "":
                    total_value = total_value + int(clean_price)
                    has_valid_price = True

    if not has_valid_price:
        print("Tổng giá trị các mặt hàng hiện tại là: 0 VND.")
        return
        
    print(f"Tổng giá trị các mặt hàng hiện tại là: {total_value:,} VND.")


def main():
    while True:
        print("\n============= E-COMMERCE ANALYTICS =============")
        print("1. Hiển thị tem nhãn sản phẩm (format_map & F-String)")
        print("2. Sắp xếp sản phẩm thông minh (vòng lặp)")
        print("3. Tính tổng giá trị kho hàng (vòng lặp)")
        print("4. Đóng hệ thống")
        print("================================================")
        
        choice = input("Chọn chức năng (1-4): ").strip()
        
        if choice == "1":
            print_product_labels()
        elif choice == "2":
            sort_products()
        elif choice == "3":
            calculate_total_value()
        elif choice == "4":
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


if __name__ == "__main__":
    main()
