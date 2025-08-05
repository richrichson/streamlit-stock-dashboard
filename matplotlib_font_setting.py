import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform

# 한글 폰트 설정 (Windows용)
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')  # 윈도우 기본 한글 폰트
else:
    plt.rc('font', family='AppleGothic')    # Mac용

# 마이너스 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False