def collision_detect(box1, box1_x, box1_y, box2):
    side_left1 = box1_x
    side_right1 = box1_x + box1.width
    side_top1 = box1_y
    side_bottom1 = box1_y + box1.height

    side_left2 = box2.x
    side_right2 = box2.x + box2.width
    side_top2 = box2.y
    side_bottom2 = box2.y + box2.height

    if side_right1 > side_left2 > side_left1 or side_right1 > side_right2 > side_left1 or (side_right1 == side_right2 and side_left1 == side_left2):  # are x sides of box1 in box2
        if side_bottom1 > side_top2 > side_top1 or side_bottom1 > side_bottom2 > side_top1 or (side_bottom1 == side_bottom2 and side_top1 == side_top2):  # ^ but for y sides
            return True
    # not redundant, needed for different sizes
    if side_right2 > side_left1 > side_left2 or side_right2 > side_right1 > side_left2:  # are x sides of box2 in box1
        if side_bottom2 > side_top1 > side_top2 or side_bottom2 > side_bottom1 > side_top2:  # ^ but for y sides
            return True


def collision_single_axis_x(entity1, entity2):
    if entity1.x_velocity > 0:
        entity1.x = entity2.x - entity1.width
    elif entity1.x_velocity < 0:
        entity1.x = entity2.x + entity2.width
    # entity1.x_velocity = 0


def collision_single_axis_y(entity1, entity2):
    if entity1.y_velocity > 0:
        entity1.y = entity2.y - entity1.height
    elif entity1.y_velocity < 0:
        entity1.y = entity2.y + entity2.height
    # entity1.y_velocity = 0


def collision_system(mover, entity):
    if collision_detect(mover, mover.x, mover.y, entity):
        if collision_detect(mover, mover.x, mover.y_past, entity):
            collision_single_axis_x(mover, entity)
        if collision_detect(mover, mover.x, mover.y, entity):
            collision_single_axis_y(mover, entity)


def collision_resolveold(mover, entity):
    mover_x1 = mover.x_past
    mover_x2 = mover.x
    mover_y1 = mover.y_past
    mover_y2 = mover.y

    entity_pos = (entity.x, entity.y)
    entity_pos2 = (entity.x + entity.x_length, entity.y + entity.y_length)

    delta_y = mover_y2 - mover_y1  # calculating change in x and y
    delta_x = mover_x2 - mover_x1

    if delta_y > 0:  # calculates the step direction for resolution for loop
        loop_delta_y = 1
    else:
        loop_delta_y = -1  # defaults to -1, but doesn't matter, only used in event of motion

    if delta_x > 0:
        loop_delta_x = 1
    else:
        loop_delta_x = -1

    if not delta_x and not delta_y:  # if there is not x or y change, the player isn't moving
        print("No motion")

    elif not delta_x and delta_y:  # if there is no change in x, the player is moving only on y axis
        print("X =", mover_x1)

        base_x = mover_x1
        end_loop = False
        # for loop from 3 to 5 will only loop through 3 to 4, 1 needs to be added in the appropriate direction
        # step number is either +1 or -1 depending on the loop_delta value
        print(mover_y1, mover_y2)
        for i in range(mover_y1, mover_y2 + loop_delta_y, loop_delta_y):
            if end_loop:
                break
            coords = ((base_x, i), (base_x + mover.x_length, i), (base_x, i + mover.y_length), (base_x + mover.x_length, i + mover.y_length))
            for j in coords:
                x = j[0]
                y = j[1]
                if x == entity_pos[0] or x == entity_pos2[0] and entity_pos[1] <= x <= entity_pos2[1]:
                    mover.x = base_x
                    mover.y = int(i)
                    end_loop = True
                    break
                if y == entity_pos[1] or y == entity_pos2[1] and entity_pos[0] <= y <= entity_pos2[0]:
                    mover.x = base_x
                    mover.y = int(i)
                    end_loop = True
                    break

    elif delta_x and not delta_y:  # if there is no change in y, the player is moving only on x axis
        print("Y =", mover_y1)

        base_y = mover_y1
        end_loop = False
        # for loop from 3 to 5 will only loop through 3 to 4, 1 needs to be added in the appropriate direction
        # step number is either +1 or -1 depending on the loop_delta value
        print(mover_y1, mover_y2)
        for i in range(mover_x1, mover_x2 + loop_delta_x, loop_delta_x):
            if end_loop:
                break
            coords = ((base_y, i), (base_y + mover.y_length, i), (base_y, i + mover.x_length),
                      (base_y + mover.y_length, i + mover.x_length))
            for j in coords:
                x = j[0]
                y = j[1]
                if x == entity_pos[0] or x == entity_pos2[0] and entity_pos[1] <= x <= entity_pos2[1]:
                    mover.x = int(i)
                    mover.y = base_y
                    end_loop = True
                    break
                if y == entity_pos[1] or y == entity_pos2[1] and entity_pos[0] <= y <= entity_pos2[0]:
                    mover.x = int(i)
                    mover.y = base_y
                    end_loop = True
                    break

    else:  # if there is a change in x and y, the linear equation is found
        slope = delta_y / delta_x
        intercept = mover_y1 - mover_x1 * slope
        slope2 = (mover_y2 - mover_y1) / (mover_x2 - mover_x1)  # calculates slope based on two points
        intercept2 = mover_y1 - mover_x1 * slope  # calculates y intercept for linear equation

        print(slope, slope2, intercept, intercept2)

        # print("y = " + str(round(slope, 3)) + "x + " + str(round(intercept, 3)))
        end_loop = False

        for x in range(mover_x1, mover_x2 + loop_delta_x, loop_delta_x):
            if end_loop:
                break
            y = slope * x + intercept
            coords = ((x, y), (x + mover.x_length, y), (x, y + mover.y_length), (x + mover.x_length, y + mover.y_length))
            # print(coords)
            for c in coords:
                xs = round(c[0])
                ys = round(c[1])
                if xs == entity_pos[0] or xs == entity_pos2[0] and entity_pos[1] <= xs <= entity_pos2[1]:
                    mover.x = x
                    mover.y = int(y)
                    end_loop = True
                    break
                if ys == entity_pos[1] or ys == entity_pos2[1] and entity_pos[0] <= ys <= entity_pos2[0]:
                    mover.x = x
                    mover.y = int(y)
                    end_loop = True
                    break
