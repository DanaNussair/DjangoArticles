class CommonCategoryServices():
  def handle_args(self, args={}):
    new_args = {}
    if args.get('title'):
      new_args['title'] = args.get('title')
    if args.get('description'):
      new_args['description'] = args.get('description')

    return new_args

  def handle_order_by(self, args={}):
    order_by= []
    if args.get('sort_by'):
      order_by.append(args.get('sort_by'))
    return order_by
