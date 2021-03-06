# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from facebook_ads.models import AdStatistic

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'AdGroup.targeting'
        db.alter_column('facebook_ads_adgroup', 'targeting_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, null=True, to=orm['facebook_ads.Targeting']))

        # Changing field 'AdGroup.adgroup_status'
        db.alter_column('facebook_ads_adgroup', 'adgroup_status', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AdGroup.bid_type'
        db.alter_column('facebook_ads_adgroup', 'bid_type', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AdGroup.updated_time'
        db.alter_column('facebook_ads_adgroup', 'updated_time', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'AdGroup.ad_status'
        db.alter_column('facebook_ads_adgroup', 'ad_status', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AdGroup.ad_id'
        db.alter_column('facebook_ads_adgroup', 'ad_id', self.gf('django.db.models.fields.BigIntegerField')(null=True))

        # Changing field 'AdGroup.creative'
        db.alter_column('facebook_ads_adgroup', 'creative_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['facebook_ads.AdCreative']))

        # Changing field 'AdGroup.max_bid'
        db.alter_column('facebook_ads_adgroup', 'max_bid', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Adding field 'AdStatistic.social_reach'
        db.add_column('facebook_ads_adstatistic', 'social_reach', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'AdStatistic.ctr'
        db.add_column('facebook_ads_adstatistic', 'ctr', self.gf('django.db.models.fields.FloatField')(default=0), keep_default=False)

        # Adding field 'AdStatistic.social'
        db.add_column('facebook_ads_adstatistic', 'social', self.gf('django.db.models.fields.FloatField')(default=0), keep_default=False)

        # Adding field 'AdStatistic.social_ctr'
        db.add_column('facebook_ads_adstatistic', 'social_ctr', self.gf('django.db.models.fields.FloatField')(default=0), keep_default=False)

        # Adding field 'AdStatistic.cpc'
        db.add_column('facebook_ads_adstatistic', 'cpc', self.gf('django.db.models.fields.FloatField')(default=0), keep_default=False)

        # Adding field 'AdStatistic.cpm'
        db.add_column('facebook_ads_adstatistic', 'cpm', self.gf('django.db.models.fields.FloatField')(default=0), keep_default=False)

        # Changing field 'AdStatistic.unique_impressions'
        db.alter_column('facebook_ads_adstatistic', 'unique_impressions', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AdStatistic.spent'
        db.alter_column('facebook_ads_adstatistic', 'spent', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'AdStatistic.actions'
        db.alter_column('facebook_ads_adstatistic', 'actions', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AdStatistic.social_unique_clicks'
        db.alter_column('facebook_ads_adstatistic', 'social_unique_clicks', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AdStatistic.social_unique_impressions'
        db.alter_column('facebook_ads_adstatistic', 'social_unique_impressions', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AdStatistic.social_spent'
        db.alter_column('facebook_ads_adstatistic', 'social_spent', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'AdStatistic.unique_clicks'
        db.alter_column('facebook_ads_adstatistic', 'unique_clicks', self.gf('django.db.models.fields.IntegerField')(null=True))

        # generate new auto-estimated fields
        for stat in AdStatistic.objects.all():
            stat.save()

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'AdGroup.targeting'
        raise RuntimeError("Cannot reverse this migration. 'AdGroup.targeting' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'AdGroup.adgroup_status'
        raise RuntimeError("Cannot reverse this migration. 'AdGroup.adgroup_status' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'AdGroup.bid_type'
        raise RuntimeError("Cannot reverse this migration. 'AdGroup.bid_type' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'AdGroup.updated_time'
        raise RuntimeError("Cannot reverse this migration. 'AdGroup.updated_time' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'AdGroup.ad_status'
        raise RuntimeError("Cannot reverse this migration. 'AdGroup.ad_status' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'AdGroup.ad_id'
        raise RuntimeError("Cannot reverse this migration. 'AdGroup.ad_id' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'AdGroup.creative'
        raise RuntimeError("Cannot reverse this migration. 'AdGroup.creative' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'AdGroup.max_bid'
        raise RuntimeError("Cannot reverse this migration. 'AdGroup.max_bid' and its values cannot be restored.")

        # Deleting field 'AdStatistic.social_reach'
        db.delete_column('facebook_ads_adstatistic', 'social_reach')

        # Deleting field 'AdStatistic.ctr'
        db.delete_column('facebook_ads_adstatistic', 'ctr')

        # Deleting field 'AdStatistic.social'
        db.delete_column('facebook_ads_adstatistic', 'social')

        # Deleting field 'AdStatistic.social_ctr'
        db.delete_column('facebook_ads_adstatistic', 'social_ctr')

        # Deleting field 'AdStatistic.cpc'
        db.delete_column('facebook_ads_adstatistic', 'cpc')

        # Deleting field 'AdStatistic.cpm'
        db.delete_column('facebook_ads_adstatistic', 'cpm')

        # User chose to not deal with backwards NULL issues for 'AdStatistic.unique_impressions'
        raise RuntimeError("Cannot reverse this migration. 'AdStatistic.unique_impressions' and its values cannot be restored.")

        # Changing field 'AdStatistic.spent'
        db.alter_column('facebook_ads_adstatistic', 'spent', self.gf('django.db.models.fields.IntegerField')())

        # User chose to not deal with backwards NULL issues for 'AdStatistic.actions'
        raise RuntimeError("Cannot reverse this migration. 'AdStatistic.actions' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'AdStatistic.social_unique_clicks'
        raise RuntimeError("Cannot reverse this migration. 'AdStatistic.social_unique_clicks' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'AdStatistic.social_unique_impressions'
        raise RuntimeError("Cannot reverse this migration. 'AdStatistic.social_unique_impressions' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'AdStatistic.social_spent'
        raise RuntimeError("Cannot reverse this migration. 'AdStatistic.social_spent' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'AdStatistic.unique_clicks'
        raise RuntimeError("Cannot reverse this migration. 'AdStatistic.unique_clicks' and its values cannot be restored.")


    models = {
        'facebook_ads.adaccount': {
            'Meta': {'ordering': "['account_id']", 'object_name': 'AdAccount'},
            'account_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'}),
            'account_status': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True'}),
            'business_city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'business_country_code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'business_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'business_state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'business_street': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'business_street2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'business_zip': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'daily_spend_limit': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_personal': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'timezone_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'timezone_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'vat_status': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'facebook_ads.adcampaign': {
            'Meta': {'ordering': "['name']", 'object_name': 'AdCampaign'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'adcampaigns'", 'to': "orm['facebook_ads.AdAccount']"}),
            'campaign_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'}),
            'campaign_status': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True'}),
            'daily_budget': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'daily_imps': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lifetime_budget': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'updated_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        'facebook_ads.adcreative': {
            'Meta': {'ordering': "['creative_id']", 'object_name': 'AdCreative'},
            'auto_update': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'body': ('django.db.models.fields.CharField', [], {'max_length': '135'}),
            'count_current_adgroups': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'creative_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_hash': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '100'}),
            'link_url': ('django.db.models.fields.URLField', [], {'max_length': '1024'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'object_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'preview_url': ('django.db.models.fields.URLField', [], {'max_length': '100'}),
            'related_fan_page': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'run_status': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True'}),
            'story_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'type': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'view_tag': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'facebook_ads.adgroup': {
            'Meta': {'ordering': "['name']", 'object_name': 'AdGroup'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'adgroups'", 'to': "orm['facebook_ads.AdAccount']"}),
            'ad_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'ad_status': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'adgroup_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'}),
            'adgroup_status': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'bid_type': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'adgroups'", 'to': "orm['facebook_ads.AdCampaign']"}),
            'creative': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'adgroups'", 'null': 'True', 'to': "orm['facebook_ads.AdCreative']"}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_bid': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'targeting': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'adgroup'", 'unique': 'True', 'null': 'True', 'to': "orm['facebook_ads.Targeting']"}),
            'updated_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        'facebook_ads.adimage': {
            'Meta': {'object_name': 'AdImage'},
            'hash': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': "'32'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': "'100'"})
        },
        'facebook_ads.adstatistic': {
            'Meta': {'ordering': "['statistic_id']", 'object_name': 'AdStatistic'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'adstatistics'", 'null': 'True', 'to': "orm['facebook_ads.AdAccount']"}),
            'actions': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'adgroup': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'adstatistics'", 'null': 'True', 'to': "orm['facebook_ads.AdGroup']"}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'adstatistics'", 'null': 'True', 'to': "orm['facebook_ads.AdCampaign']"}),
            'clicks': ('django.db.models.fields.IntegerField', [], {}),
            'connections': ('django.db.models.fields.IntegerField', [], {}),
            'cpc': ('django.db.models.fields.FloatField', [], {}),
            'cpm': ('django.db.models.fields.FloatField', [], {}),
            'ctr': ('django.db.models.fields.FloatField', [], {}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impressions': ('django.db.models.fields.IntegerField', [], {}),
            'social': ('django.db.models.fields.FloatField', [], {}),
            'social_clicks': ('django.db.models.fields.IntegerField', [], {}),
            'social_ctr': ('django.db.models.fields.FloatField', [], {}),
            'social_impressions': ('django.db.models.fields.IntegerField', [], {}),
            'social_reach': ('django.db.models.fields.IntegerField', [], {}),
            'social_spent': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'social_unique_clicks': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'social_unique_impressions': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'spent': ('django.db.models.fields.FloatField', [], {}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'statistic_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': "'100'"}),
            'unique_clicks': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'unique_impressions': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'facebook_ads.aduser': {
            'Meta': {'ordering': "['role']", 'unique_together': "(('account', 'uid'),)", 'object_name': 'AdUser'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'users'", 'to': "orm['facebook_ads.AdAccount']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'permissions': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '20'}),
            'role': ('django.db.models.fields.IntegerField', [], {}),
            'uid': ('django.db.models.fields.BigIntegerField', [], {})
        },
        'facebook_ads.targeting': {
            'Meta': {'object_name': 'Targeting'},
            'age_max': ('facebook_ads.fields.PositiveSmallIntegerRangeField', [], {'null': 'True', 'blank': 'True'}),
            'age_min': ('facebook_ads.fields.PositiveSmallIntegerRangeField', [], {'null': 'True', 'blank': 'True'}),
            'broad_age': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'cities': ('annoying.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'college_majors': ('facebook_ads.fields.CommaSeparatedCharField', [], {'max_length': '100'}),
            'college_networks': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'college_years': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '100'}),
            'connections': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '100'}),
            'countries': ('facebook_ads.fields.CommaSeparatedCharField', [], {'max_length': '100', 'blank': 'True'}),
            'education_statuses': ('facebook_ads.fields.CommaSeparatedCharField', [], {'max_length': '100'}),
            'excluded_connections': ('annoying.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'friends_of_connections': ('annoying.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'genders': ('facebook_ads.fields.CommaSeparatedCharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interested_in': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'keywords': ('facebook_ads.fields.CommaSeparatedCharField', [], {'max_length': '4000'}),
            'locales': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'radius': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'regions': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'relationship_statuses': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user_adclusters': ('annoying.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'user_event': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '100'}),
            'work_networks': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'zips': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['facebook_ads']
