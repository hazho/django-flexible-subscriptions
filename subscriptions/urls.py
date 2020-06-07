"""URLs for the Flexible Subscriptions app."""
# pylint: disable=line-too-long
import importlib

from django.conf.urls import url

from subscriptions import views
from subscriptions.conf import SETTINGS


# Retrieve the proper subscribe view
SubscribeView = getattr(  # pylint: disable=invalid-name
    importlib.import_module(SETTINGS['subscribe_view']['module']),
    SETTINGS['subscribe_view']['class']
)


urlpatterns = [
    url(
        r'^subscribe/$',
        views.SubscribeList.as_view(),
        name='dfs_subscribe_list',
    ),
    url(
        r'^subscribe/add/$',
        SubscribeView.as_view(),
        name='dfs_subscribe_add',
    ),
    url(
        r'^subscribe/thank-you/(?P<transaction_id>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})/$',  # noqa
        views.SubscribeThankYouView.as_view(),
        name='dfs_subscribe_thank_you',
    ),
    url(
        r'^subscribe/cancel/(?P<subscription_id>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})/$',  # noqa
        views.SubscribeCancelView.as_view(),
        name='dfs_subscribe_cancel',
    ),
    url(
        r'^subscriptions/$',
        views.SubscribeUserList.as_view(),
        name='dfs_subscribe_user_list',
    ),
    url(
        r'^dfs/tags/$',
        views.TagListView.as_view(),
        name='dfs_tag_list',
    ),
    url(
        r'^dfs/tags/create/$',
        views.TagCreateView.as_view(),
        name='dfs_tag_create',
    ),
    url(
        r'^dfs/tags/(?P<tag_id>[0-9]+)/$',
        views.TagUpdateView.as_view(),
        name='dfs_tag_update',
    ),
    url(
        r'^dfs/tags/(?P<tag_id>[0-9]+)/delete/$',
        views.TagDeleteView.as_view(),
        name='dfs_tag_delete',
    ),
    url(
        r'^dfs/plans/$',
        views.PlanListView.as_view(),
        name='dfs_plan_list',
    ),
    url(
        r'^dfs/plans/create/$',
        views.PlanCreateView.as_view(),
        name='dfs_plan_create',
    ),
    url(
        r'^dfs/plans/(?P<plan_id>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})/$',
        views.PlanUpdateView.as_view(),
        name='dfs_plan_update',
    ),
    url(
        r'^dfs/plans/(?P<plan_id>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})/delete/$',
        views.PlanDeleteView.as_view(),
        name='dfs_plan_delete',
    ),
    url(
        r'^dfs/plan-lists/$',
        views.PlanListListView.as_view(),
        name='dfs_plan_list_list',
    ),
    url(
        r'^dfs/plan-lists/create/$',
        views.PlanListCreateView.as_view(),
        name='dfs_plan_list_create',
    ),
    url(
        r'^dfs/plan-lists/(?P<plan_list_id>[0-9]+)/$',
        views.PlanListUpdateView.as_view(),
        name='dfs_plan_list_update',
    ),
    url(
        r'^dfs/plan-lists/(?P<plan_list_id>[0-9]+)/delete/$',
        views.PlanListDeleteView.as_view(),
        name='dfs_plan_list_delete',
    ),
    url(
        r'^dfs/plan-lists/(?P<plan_list_id>[0-9]+)/details/$',
        views.PlanListDetailListView.as_view(),
        name='dfs_plan_list_detail_list',
    ),
    url(
        r'^dfs/plan-lists/(?P<plan_list_id>[0-9]+)/details/create/$',
        views.PlanListDetailCreateView.as_view(),
        name='dfs_plan_list_detail_create',
    ),
    url(
        r'^dfs/plan-lists/(?P<plan_list_id>[0-9]+)/details/(?P<plan_list_detail_id>[0-9]+)/$',
        views.PlanListDetailUpdateView.as_view(),
        name='dfs_plan_list_detail_update',
    ),
    url(
        r'^dfs/plan-lists/(?P<plan_list_id>[0-9]+)/details/(?P<plan_list_detail_id>[0-9]+)/delete/$',
        views.PlanListDetailDeleteView.as_view(),
        name='dfs_plan_list_detail_delete',
    ),
    url(
        r'^dfs/subscriptions/$',
        views.SubscriptionListView.as_view(),
        name='dfs_subscription_list',
    ),
    url(
        r'^dfs/subscriptions/create/$',
        views.SubscriptionCreateView.as_view(),
        name='dfs_subscription_create',
    ),
    url(
        r'^dfs/subscriptions/(?P<subscription_id>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})/$',  # noqa
        views.SubscriptionUpdateView.as_view(),
        name='dfs_subscription_update',
    ),
    url(
        r'^dfs/subscriptions/(?P<subscription_id>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})/delete/$',  # noqa
        views.SubscriptionDeleteView.as_view(),
        name='dfs_subscription_delete',
    ),
    url(
        r'^dfs/transactions/$',
        views.TransactionListView.as_view(),
        name='dfs_transaction_list',
    ),
    url(
        r'^dfs/transactions/(?P<transaction_id>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})/$',  # noqa
        views.TransactionDetailView.as_view(),
        name='dfs_transaction_detail',
    ),
    url(
        r'^dfs/$',
        views.DashboardView.as_view(),
        name='dfs_dashboard',
    ),
]
