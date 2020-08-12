def eat(food, is_healthy):
        if not isinstance(is_healthy, bool):
            raise ValueError("must be boolean")
        ending = "because YOLO"
        if is_healthy:
            ending = "because my body is a temple"
        return f"I'm eating {food}, {ending}"




def nap(num_hours):
    if num_hours > 2:
        return f"Ugh I overslept. I didn't mean to nap so long"
    else:
        return f"I'm feeling refreshed after my {num_hours} hour nap"


