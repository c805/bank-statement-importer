def print_validation_results(errors, warnings):

    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"  - {error}")

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"  - {warning}")

    if not errors and not warnings:
        print("\nValidation passed.")