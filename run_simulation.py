
import argparse
import json
from main import decide_action


def run_simulation(scenario_file):
    with open(scenario_file, "r", encoding="utf-8") as file:
        scenario = json.load(file)

    print("Simulation:", scenario["scenario_name"])
    print("-" * 45)

    passed = 0
    total = len(scenario["test_cases"])

    for index, case in enumerate(scenario["test_cases"], 1):
        distance = case["distance"]
        expected = case["expected_action"]
        actual = decide_action(distance)

        status = "PASSED" if actual == expected else "FAILED"

        if status == "PASSED":
            passed += 1

        print(
            f"Test {index}: Distance={distance}m | "
            f"Expected={expected} | Actual={actual} | {status}"
        )

    print("-" * 45)
    print(f"Results: {passed}/{total} tests passed")

    return passed == total


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", required=True)
    args = parser.parse_args()

    success = run_simulation(args.scenario)

    if not success:
        raise SystemExit(1)
