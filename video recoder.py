import cv2

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(0)

# 코덱 및 비디오 파일 저장 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 코덱 설정
fps = 20.0  # 프레임 속도
frame_size = (int(cap.get(3)), int(cap.get(4)))
out = cv2.VideoWriter('output.avi', fourcc, fps, frame_size)

recording = False  # 녹화 상태
brightness = 1.0  # 밝기 조정 값

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # 밝기 조정 필터 적용
    frame = cv2.convertScaleAbs(frame, alpha=brightness, beta=0)
    
    if recording:
        out.write(frame)
        # 녹화 중임을 나타내는 빨간색 원 표시
        cv2.circle(frame, (50, 50), 20, (0, 0, 255), -1)
    
    cv2.imshow('Video Recorder', frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == 27:  # ESC 키로 종료
        break
    elif key == 32:  # Space 키로 녹화 모드 전환
        recording = not recording
    elif key == ord('+'):  # 밝기 증가
        brightness = min(brightness + 0.1, 2.0)
    elif key == ord('-'):  # 밝기 감소
        brightness = max(brightness - 0.1, 0.5)

# 자원 해제
cap.release()
out.release()
cv2.destroyAllWindows()