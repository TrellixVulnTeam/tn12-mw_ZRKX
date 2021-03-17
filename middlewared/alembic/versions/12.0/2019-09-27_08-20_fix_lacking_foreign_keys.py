"""Fix lacking foreign keys

Revision ID: d38e9cc6174c
Revises: a3423860aea0
Create Date: 2019-09-27 08:20:13.391318+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd38e9cc6174c'
down_revision = 'a3423860aea0'
branch_labels = None
depends_on = None


def create_foreign_key(*args, **kwargs):
    op.execute(f"DELETE FROM {args[1]} WHERE {args[3][0]} NOT IN (SELECT {args[4][0]} FROM {args[2]})")


def create_foreign_key_nullable(*args, **kwargs):
    op.execute(f"UPDATE {args[1]} SET {args[3][0]} = NULL WHERE {args[3][0]} IS NOT NULL AND {args[3][0]} NOT IN (SELECT {args[4][0]} FROM {args[2]})")


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    create_foreign_key(None, 'account_bsdgroupmembership', 'account_bsdgroups', ['bsdgrpmember_group_id'], ['id'])
    create_foreign_key(None, 'account_bsdgroupmembership', 'account_bsdusers', ['bsdgrpmember_user_id'], ['id'])
    with op.batch_alter_table('account_bsdgroupmembership', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_account_bsdgroupmembership_bsdgrpmember_group_id_account_bsdgroups'), 'account_bsdgroups', ['bsdgrpmember_group_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(batch_op.f('fk_account_bsdgroupmembership_bsdgrpmember_user_id_account_bsdusers'), 'account_bsdusers', ['bsdgrpmember_user_id'], ['id'], ondelete='CASCADE')

    create_foreign_key_nullable(None, 'directoryservice_activedirectory', 'directoryservice_kerberosrealm', ['ad_kerberos_realm_id'], ['id'])
    with op.batch_alter_table('directoryservice_activedirectory', schema=None) as batch_op:
        batch_op.drop_references('ad_kerberos_realm_id')
        batch_op.create_foreign_key(batch_op.f('fk_directoryservice_activedirectory_ad_kerberos_realm_id_directoryservice_kerberosrealm'), 'directoryservice_kerberosrealm', ['ad_kerberos_realm_id'], ['id'], ondelete='SET NULL')

    create_foreign_key(None, 'network_alias', 'network_interfaces', ['alias_interface_id'], ['id'])
    with op.batch_alter_table('network_alias', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_network_alias_alias_interface_id_network_interfaces'), 'network_interfaces', ['alias_interface_id'], ['id'], ondelete='CASCADE')

    create_foreign_key(None, 'network_bridge', 'network_interfaces', ['interface_id'], ['id'])
    with op.batch_alter_table('network_bridge', schema=None) as batch_op:
        batch_op.drop_references('interface_id')
        batch_op.create_foreign_key(batch_op.f('fk_network_bridge_interface_id_network_interfaces'), 'network_interfaces', ['interface_id'], ['id'], ondelete='CASCADE')

    create_foreign_key(None, 'network_lagginterface', 'network_interfaces', ['lagg_interface_id'], ['id'])
    with op.batch_alter_table('network_lagginterface', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_network_lagginterface_lagg_interface_id_network_interfaces'), 'network_interfaces', ['lagg_interface_id'], ['id'])

    create_foreign_key(None, 'network_lagginterfacemembers', 'network_lagginterface', ['lagg_interfacegroup_id'], ['id'])
    with op.batch_alter_table('network_lagginterfacemembers', schema=None) as batch_op:
        batch_op.drop_references('lagg_interfacegroup_id')
        batch_op.create_foreign_key(batch_op.f('fk_network_lagginterfacemembers_lagg_interfacegroup_id_network_lagginterface'), 'network_lagginterface', ['lagg_interfacegroup_id'], ['id'], ondelete='CASCADE')

    create_foreign_key_nullable(None, 'services_fibrechanneltotarget', 'services_iscsitarget', ['fc_target_id'], ['id'])
    with op.batch_alter_table('services_fibrechanneltotarget', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_services_fibrechanneltotarget_fc_target_id_services_iscsitarget'), 'services_iscsitarget', ['fc_target_id'], ['id'])

    create_foreign_key_nullable(None, 'services_iscsitargetgroups', 'services_iscsitargetauthorizedinitiator', ['iscsi_target_initiatorgroup_id'], ['id'])
    create_foreign_key(None, 'services_iscsitargetgroups', 'services_iscsitarget', ['iscsi_target_id'], ['id'])
    create_foreign_key(None, 'services_iscsitargetgroups', 'services_iscsitargetportal', ['iscsi_target_portalgroup_id'], ['id'])
    with op.batch_alter_table('services_iscsitargetgroups', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_services_iscsitargetgroups_iscsi_target_initiatorgroup_id_services_iscsitargetauthorizedinitiator'), 'services_iscsitargetauthorizedinitiator', ['iscsi_target_initiatorgroup_id'], ['id'], ondelete='SET NULL')
        batch_op.create_foreign_key(batch_op.f('fk_services_iscsitargetgroups_iscsi_target_id_services_iscsitarget'), 'services_iscsitarget', ['iscsi_target_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_services_iscsitargetgroups_iscsi_target_portalgroup_id_services_iscsitargetportal'), 'services_iscsitargetportal', ['iscsi_target_portalgroup_id'], ['id'])

    create_foreign_key(None, 'services_iscsitargetportalip', 'services_iscsitargetportal', ['iscsi_target_portalip_portal_id'], ['id'])
    with op.batch_alter_table('services_iscsitargetportalip', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_services_iscsitargetportalip_iscsi_target_portalip_portal_id_services_iscsitargetportal'), 'services_iscsitargetportal', ['iscsi_target_portalip_portal_id'], ['id'])

    create_foreign_key_nullable(None, 'services_webdav', 'system_certificate', ['webdav_certssl_id'], ['id'])
    with op.batch_alter_table('services_webdav', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_services_webdav_webdav_certssl_id_system_certificate'), 'system_certificate', ['webdav_certssl_id'], ['id'])

    create_foreign_key(None, 'storage_encrypteddisk', 'storage_volume', ['encrypted_volume_id'], ['id'])
    create_foreign_key_nullable(None, 'storage_encrypteddisk', 'storage_disk', ['encrypted_disk_id'], ['disk_identifier'])
    with op.batch_alter_table('storage_encrypteddisk', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_storage_encrypteddisk_encrypted_volume_id_storage_volume'), 'storage_volume', ['encrypted_volume_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_storage_encrypteddisk_encrypted_disk_id_storage_disk'), 'storage_disk', ['encrypted_disk_id'], ['disk_identifier'], ondelete='SET NULL')

    create_foreign_key(None, 'storage_scrub', 'storage_volume', ['scrub_volume_id'], ['id'])
    with op.batch_alter_table('storage_scrub', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_storage_scrub_scrub_volume_id_storage_volume'), 'storage_volume', ['scrub_volume_id'], ['id'])

    create_foreign_key(None, 'tasks_smarttest_smarttest_disks', 'storage_disk', ['disk_id'], ['disk_identifier'], ondelete='CASCADE')
    create_foreign_key(None, 'tasks_smarttest_smarttest_disks', 'tasks_smarttest', ['smarttest_id'], ['id'], ondelete='CASCADE')
    with op.batch_alter_table('tasks_smarttest_smarttest_disks', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_tasks_smarttest_smarttest_disks_disk_id_storage_disk'), 'storage_disk', ['disk_id'], ['disk_identifier'], ondelete='CASCADE')
        batch_op.create_foreign_key(batch_op.f('fk_tasks_smarttest_smarttest_disks_smarttest_id_tasks_smarttest'), 'tasks_smarttest', ['smarttest_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks_smarttest_smarttest_disks', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_tasks_smarttest_smarttest_disks_smarttest_id_tasks_smarttest'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_tasks_smarttest_smarttest_disks_disk_id_storage_disk'), type_='foreignkey')

    with op.batch_alter_table('storage_scrub', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_storage_scrub_scrub_volume_id_storage_volume'), type_='foreignkey')

    with op.batch_alter_table('storage_encrypteddisk', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_storage_encrypteddisk_encrypted_disk_id_storage_disk'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_storage_encrypteddisk_encrypted_volume_id_storage_volume'), type_='foreignkey')

    with op.batch_alter_table('services_webdav', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_services_webdav_webdav_certssl_id_system_certificate'), type_='foreignkey')

    with op.batch_alter_table('services_iscsitargetportalip', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_services_iscsitargetportalip_iscsi_target_portalip_portal_id_services_iscsitargetportal'), type_='foreignkey')

    with op.batch_alter_table('services_iscsitargetgroups', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_services_iscsitargetgroups_iscsi_target_portalgroup_id_services_iscsitargetportal'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_services_iscsitargetgroups_iscsi_target_id_services_iscsitarget'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_services_iscsitargetgroups_iscsi_target_initiatorgroup_id_services_iscsitargetauthorizedinitiator'), type_='foreignkey')

    with op.batch_alter_table('services_fibrechanneltotarget', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_services_fibrechanneltotarget_fc_target_id_services_iscsitarget'), type_='foreignkey')

    with op.batch_alter_table('network_lagginterfacemembers', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_network_lagginterfacemembers_lagg_interfacegroup_id_network_lagginterface'), type_='foreignkey')

    with op.batch_alter_table('network_lagginterface', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_network_lagginterface_lagg_interface_id_network_interfaces'), type_='foreignkey')

    with op.batch_alter_table('network_bridge', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_network_bridge_interface_id_network_interfaces'), type_='foreignkey')

    with op.batch_alter_table('network_alias', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_network_alias_alias_interface_id_network_interfaces'), type_='foreignkey')

    with op.batch_alter_table('directoryservice_activedirectory', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_directoryservice_activedirectory_ad_kerberos_realm_id_directoryservice_kerberosrealm'), type_='foreignkey')

    with op.batch_alter_table('account_bsdgroupmembership', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_account_bsdgroupmembership_bsdgrpmember_user_id_account_bsdusers'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_account_bsdgroupmembership_bsdgrpmember_group_id_account_bsdgroups'), type_='foreignkey')

    # ### end Alembic commands ###
