from tensorboard.backend.event_processing.event_accumulator import EventAccumulator

event_acc = EventAccumulator('result/logs/events.out.tfevents.1563926837.DL-Server')
event_acc.Reload()
# Show all tags in the log file
print(event_acc.Tags())

# E. g. get wall clock, number of steps and value for a scalar 'Accuracy'
w_times, step_nums, vals = zip(*event_acc.Scalars('train_elbo'))

print("step_nums---w_times---vals")
for i in range(len(w_times)):
	print(str(step_nums[i]) + "---" + str(w_times[i]) + "---" + str(vals[i]))
