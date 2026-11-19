// MongoDB examples (mongosh) - heat exchanger data
db.exchanger.find({ fouling_pct: { $gt: 5 } })
db.exchanger.aggregate([{ $group: { _id: '$Type', avgU: { $avg: '$U' } } }])
db.exchanger.aggregate([{ $group: { _id: '$Month', saving: { $sum: '$saving_usd' } } }, { $sort: { _id: 1 } }])
