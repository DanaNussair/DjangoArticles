class CommonArticlesServices():
  def handle_args(self, args={}):
    new_args = {**args}
    if args.get('category_title'):
      del new_args['category_title']
      new_args['category__title'] = args.get('category_title')

    return new_args

  def handle_order_by(self, args={}):
    order_by= []
    if args.get('sort_by'):
      order_by.append(args.get('sort_by'))
    return order_by
