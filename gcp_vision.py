import os
import cv2
def localize_objects(path):
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations
    print(objects)
    os.system('cp cyberpunk.jpeg cyberpunk_annotated.jpeg')
    img = cv2.imread('cyberpunk_annotated.jpeg') 
    for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        x1,y1 = object_.bounding_poly.normalized_vertices[0].x, object_.bounding_poly.normalized_vertices[0].y
        x2,y2 = object_.bounding_poly.normalized_vertices[2].x, object_.bounding_poly.normalized_vertices[2].y
        cv2.rectangle(img, (int(x1*img.shape[1]), int(y1*img.shape[0])), (int(x2*img.shape[1]), int(y2*img.shape[0])), (0,255,0), 2)
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))
    cv2.imwrite('cyberpunk_annotated.jpeg', img)

localize_objects('cyberpunk.jpeg')

    
