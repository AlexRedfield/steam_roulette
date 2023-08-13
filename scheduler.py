from regedit import get_running_game_id
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from db_utils import insert_data, GameSession


class DetectJob:
    def __init__(self):
        self.start_time = None
        self.status = 0

    def detect_regedit(self):
        app_id = get_running_game_id()
        if app_id != self.status:
            if self.status == 0:
                self.start_time = datetime.now()
                print(f'game {app_id} start')
            else:
                print(f'game {self.status} over')
                end_time = datetime.now()
                duration = int((end_time - self.start_time).seconds / 60)
                session = GameSession(self.status, self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
                                      end_time.strftime("%Y-%m-%d %H:%M:%S"), duration)
                insert_data(session)
                if app_id != 0:
                    self.start_time = datetime.now()
                    print(f'game {app_id} start')
            self.status = app_id


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    job = DetectJob()
    scheduler.add_job(job.detect_regedit, 'interval', seconds=60)
    scheduler.start()
