
# các biến trong Python được phân loại theo phạm vi của chúng, bao gồm:
# Local: Biến được định nghĩa trong một hàm hoặc khối mã và chỉ có thể truy cập được trong phạm vi đó.
# Enclosing: Biến được định nghĩa trong một hàm bên ngoài và có thể truy cập được trong các hàm lồng nhau.
# Global: Biến được định nghĩa ở cấp độ toàn cục và có thể truy cập được từ bất kỳ đâu trong mã.
# Built-in: Biến được định nghĩa sẵn trong Python, như `print`, `len`, v.v.
myhight= 167 # đây là global
def guess_height(height):
    #height là local, chỉ có thể truy cập trong hàm này
    if height == myhight:
        return True
    else:
        return False