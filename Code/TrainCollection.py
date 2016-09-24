#!/ user/bin/env python3

from prettytable import PrettyTable


class TrainCollection(object):

    header = 'train station time duration first second softsleep hardsleep hardsit'.split()

    def __init__(self, rows):
        self.rows = rows

    def _get_duration(self, row):
        
        duration = row.get('lishi').replace(':', 'h') + 'm'
        if duration.startswith('00'):
            return duration[4:]
        if duration.startswith('0'):
            return duration[1:]
        return duration

    @property
    def trains(self):
        for row in self.rows:
            train = [
                row['station_train_code'],
                '\n'.join([row['from_station_name'], row['to_station_name']]),
                '\n'.join([row['start_time'], row['arrive_time']]),
                self._get_duration(row),
                row['zy_num'],
                row['ze_num'],
                row['rw_num'],
                row['yw_num'],
                row['yz_num']
            ]
            yield train

    def pretty_print(self):

        pt = PrettyTable()
        pt._set_field_names(self.header)
        for train in self.trains:
            pt.add_row(train)
        print(pt)
