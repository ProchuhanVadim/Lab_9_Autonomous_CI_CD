
def decide_action(distance):
    """Визначення дії автономного робота."""
    if distance < 0:
        raise ValueError("Відстань не може бути від'ємною")

    if distance <= 1.5:
        return "STOP"
    return "MOVE"


if __name__ == "__main__":
    distances = [3.0, 1.2, 0.5, 2.5]

    print("Autonomous System Service")
    print("-------------------------")

    for distance in distances:
        action = decide_action(distance)
        print(f"Distance: {distance} m -> Action: {action}")
