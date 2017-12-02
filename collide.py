import pygame


def collision_test(rect1, rect2):
    return pygame.Rect.colliderect(rect1, rect2)


def collision_single_axis_x(entity1, entity2):
    if entity1.x_velocity_old > 0:  # if velocity is positive (right)
        entity1.rect.x = entity2.rect.x - entity1.rect.width  # set coords to the left most side of tile
    elif entity1.x_velocity_old < 0:  # if velocity is negative (left)
        entity1.rect.x = entity2.rect.x + entity2.rect.width  # set coords to the right most side of the tile
    entity1.x_velocity = 0


def collision_single_axis_y(entity1, entity2):
    if entity1.y_velocity_old > 0:
        entity1.rect.y = entity2.rect.y - entity1.rect.height
    elif entity1.y_velocity_old < 0:
        entity1.rect.y = entity2.rect.y + entity2.rect.height
    entity1.y_velocity = 0


def collision_resolve(obj1, objs):

    if obj1.x_velocity_old:  # if motion is in x direction
        obj1.update_x()  # move in x direction
        for obj in objs:  # for every collideable object
            if collision_test(obj1.rect, obj.rect):  # if there is a collision
                collision_single_axis_x(obj1, obj)  # resolve it

    elif obj1.y_velocity_old:
        obj1.update_y()
        for obj in objs:
            if collision_test(obj1.rect, obj.rect):
                collision_single_axis_y(obj1, obj)

    else:  # update x and y directions if no collision
        obj1.update_x()
        obj1.update_y()
