import pandas as pd
import numpy as np
import sys

print(f"Python版本: {sys.version}")
print(f"Pandas版本: {pd.__version__}")
print(f"NumPy版本: {np.__version__}")

# 创建一个简单的DataFrame测试
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
print("\n测试DataFrame:")
print(df)