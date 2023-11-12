from app.tasks import hello_world

if __name__ == '__main__':
    print(hello_world.delay())
    # print(f'Task ID: {result.task_id}')