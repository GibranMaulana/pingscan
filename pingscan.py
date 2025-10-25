#!/usr/bin/env python3
import cv2
import webbrowser


def main():
    print("Starting camera...")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Cannot access camera")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    qr_detector = cv2.QRCodeDetector()

    print("Camera started...")
    print("SCANNING...")

    opened_urls = set()

    try:
        while True:
            ret, frame = cap.read()

            if not ret:
                print("Failed to read from camera")
                break

            data, vertices, _ = qr_detector.detectAndDecode(frame)

            if data:
                full_url = f"https://pingfest.id/attendance/check/{data}"

                if full_url not in opened_urls:
                    opened_urls.add(full_url)

                    print(f"\nQR CODE DETECTED:")
                    print(f"Data: {full_url}")
                    print(f"Timestamp: {cv2.getTickCount()}")
                    print("-" * 30)

                    print(f"🚀 Opening URL in browser...")
                    webbrowser.open(full_url)

                if vertices is not None:
                    vertices = vertices.astype(int)
                    cv2.polylines(frame, [vertices], True, (0, 255, 0), 3)

                    cv2.putText(
                        frame,
                        "QR CODE FOUND",
                        (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 0),
                        2,
                    )

            cv2.imshow("scanning...", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q") or key == ord("Q") or key == 27:
                print("\nExiting scanner...")
                break

    except KeyboardInterrupt:
        print("\n\nkeluar")
    except Exception as e:
        print(f"\nerror: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
