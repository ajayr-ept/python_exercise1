
# emp_attandance_and_leave = {}
# emp_attandance_hour = {}
# # emp_date_of_hours = {}
emp_dict =  {
            101:{   'name': 'Anupriya Roy',
                    'depart_id':1,
                    'attendances':[{'date':1, 'hours':[3.5,4.5]},{'date':2, 'hours':[3.2,4.5]},{'date':3, 'hours':[3.2,4.6]},
                                 {'date':4, 'hours':[3.0,4.5]},{'date':5, 'hours':[2.5,4.5]},{'date':6, 'hours':[1.5,4.5]},
                                 {'date':7, 'hours':[2,3]},{'date':8, 'hours':[0,4.5]},{'date':9, 'hours':[2,3.5]},
                                 {'date':10, 'hours':[4,3.5]}],
                    'leaves':[{'date':7, 'no_of_hours':1.5},{'date':7, 'no_of_hours':1.5},{'date':8, 'no_of_hours':3}]
                },
            102: {   'name': 'Kadambari Sharma',
                 'depart_id':1,
                 'attendances':[{'date':1, 'hours': [0,4.5]},{'date':2, 'hours':[3.2,0]},{'date':3, 'hours':[3.2,4.6]},
                                {'date':4, 'hours':[1,4.5]},{'date':5, 'hours':[2.5,2]},{'date':6, 'hours':[1.5,1]},
                                {'date':7, 'hours':[2,4]},{'date':8, 'hours':[1,4.5]},{'date':9, 'hours':[2,2]},
                                {'date':10, 'hours':[2,3.5]}],
                 'leaves':[{'date':1, 'no_of_hours':3.5},{'date':2, 'no_of_hours':2},{'date':2, 'no_of_hours':2}]
             },103:
            {   'name': 'Abhishek Verma',
                'depart_id':1,
                'attendances':[{'date':3, 'hours':[3.2,4.6]},{'date':4, 'hours':[1,4.5]},{'date':5, 'hours':[2.5,2]},
                            {'date':6, 'hours':[1.5,1]},{'date':7, 'hours':[2,4]},{'date':8, 'hours':[1,4.5]},
                            {'date':9, 'hours':[2,2]},{'date':10, 'hours':[2,3.5]}
                ],
                'leaves':[{'date':1, 'no_of_hours':3},{'date':2, 'no_of_hours':2},{'date':2, 'no_of_hours':3}]
            }
}
# for key in emp_dict:
#     total_leave_days=sum(map(lambda a: a['no_of_hours'], emp_dict[key]['leaves']))
#     total_attendance_hours = sum(map(lambda a: sum(a['hours']), emp_dict[key]['attendances']))
#
#     emp_attandance_and_leave.update({'employee_id':key,
#           'employee_name':emp_dict[key]['name'],
#           'total_attendance_hours':total_attendance_hours,
#           'total_leave_days':total_leave_days})
#     print(emp_attandance_and_leave)




list_total_attendance_leave = []
list_day_wise_duty = []


for emp_key, emp_value in emp_dict.items():

        total_emp_attendense = sum(list(
            map(lambda hrslist: sum(list(filter(lambda sublist: sublist in hrslist["hours"], hrslist["hours"]))),
                emp_value["attendances"])))
        total_leave_days = sum(map(lambda leave: leave['no_of_hours'], emp_value["leaves"]))


        total_hours = list(
            map(lambda hourelist: sum(list(filter(lambda sublist: sublist in hourelist["hours"], hourelist["hours"]))),
                emp_value["attendances"]))

        date = list(filter(lambda attend: attend, list(
            map(lambda date: date.get("date") if sum(date.get("hours")) < 7 else False, emp_value["attendances"]))))

        present_hours = list(filter(lambda values: values < 7.0, total_hours))
        total_remaining_hours = list(map(lambda values: 8.0 - values, present_hours))

        list_total_attendance_leave.append(
            {"employee_id": emp_key, "employee_name": emp_value["name"], "total_attendance_hours": total_emp_attendense,
             "total_leave": total_leave_days})

        # Store day wise record of employee in list and houre details
        list_day_wise_duty.append(
            {emp_key: {"date": date, "total_hrs": present_hours, "remaining_houre": total_remaining_hours}})

        print(list_total_attendance_leave)
        print(list_day_wise_duty)