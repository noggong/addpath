### **📌 `addpath` 패키지 README (Markdown 형식, 한글 버전)**  
📢 **이 패키지는 Python에서 상위 디렉토리를 자동으로 `sys.path`에 추가하여, 불필요한 `sys.path.insert()` 호출을 줄이는 것을 목표로 합니다.**  

```markdown
# 📌 addpath - Python에서 자동으로 상위 디렉토리를 추가하는 패키지

## 🚀 소개
`addpath`는 Python에서 **상위 디렉토리를 자동으로 `sys.path`에 추가**하는 유틸리티 패키지입니다.  
더 이상 `sys.path.insert(0, "..")` 같은 코드를 반복해서 작성할 필요가 없습니다!

## 📌 설치 방법
PyPI에서 바로 설치할 수 있습니다.

```sh
pip install addpath
```

또는 GitHub에서 직접 설치할 수도 있습니다.

```sh
pip install git+https://github.com/noggong/addpath.git
```

---

## 🚀 사용법
### **1️⃣ 기본 사용법**
```python
import addpath

# 현재 스크립트의 상위 디렉토리를 sys.path에 추가
addpath.add_parent_path()
```
✅ **이제 상위 디렉토리에 있는 모듈을 바로 import할 수 있습니다!**

### **2️⃣ 특정 레벨의 상위 디렉토리 추가**
기본적으로 `add_parent_path()` 함수는 **현재 실행 중인 파일의 1단계 상위 디렉토리를 `sys.path`에 추가**합니다.  
그러나, 더 상위 디렉토리를 추가하고 싶다면 `levels` 값을 조정하면 됩니다.

```python
# 상위 디렉토리 2단계 추가
addpath.add_parent_path(levels=2)
```
✅ **이제 두 단계 위에 있는 패키지도 `import`할 수 있습니다.**

---

## 📌 예제 프로젝트 구조
```sh
my_project/
│── main.py
│── src/
│   │── my_module.py
```

📌 **예제 코드 (`src/my_module.py`)**
```python
def hello():
    return "안녕하세요! addpath를 사용하면 편리해요."
```

📌 **main.py에서 `my_module.py`를 import하는 방법**
```python
import addpath
addpath.add_parent_path()

import my_module
print(my_module.hello())  # "안녕하세요! addpath를 사용하면 편리해요."
```

✅ **더 이상 `sys.path.insert()`를 반복해서 추가할 필요가 없습니다!**

---

## 📌 자동으로 `sys.path`를 설정해야 하는 경우
- **프로젝트 구조가 복잡한 경우**
- **테스트 코드에서 부모 디렉토리의 모듈을 불러와야 할 때**
- **Jupyter Notebook에서 외부 모듈을 쉽게 불러오고 싶을 때**
- **Python 스크립트 실행 시 불필요한 `sys.path.append()` 코드 없이 실행하고 싶을 때**

---

## 🚀 기능 정리
✔ `add_parent_path(levels=1)` → 현재 디렉토리의 `levels`만큼 상위 디렉토리를 `sys.path`에 추가  
✔ `pip install addpath` → 어디서든 간편하게 설치 후 사용 가능  
✔ Python 3.6 이상 지원 🚀  

---

## 📌 라이선스
이 프로젝트는 **MIT 라이선스**로 제공됩니다. 자유롭게 사용 및 수정할 수 있습니다.  

---

## 📌 기여 방법
`addpath` 프로젝트에 기여하고 싶다면, GitHub에서 Fork 후 PR을 보내주세요! 🚀  
```sh
git clone https://github.com/yourusername/addpath.git
cd addpath
pip install -e .
```

✅ **이제 개발 환경에서 `addpath`를 테스트하고 개선할 수 있습니다.** 🚀🔥  

---

📌 **이제 Python 프로젝트에서 `sys.path` 문제를 간단하게 해결하세요!** 🚀
```

✅ **Markdown 문법이 적용된 README로, 바로 GitHub이나 PyPI에서 사용 가능합니다!** 🚀🔥