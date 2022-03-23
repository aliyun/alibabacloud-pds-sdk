// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class LogDetail extends TeaModel {
    @NameInMap("account_log_detail")
    public AccountLogDetail accountLogDetail;

    @NameInMap("audit_mgmt_log_detail")
    public AuditMgmtLogDetail auditMgmtLogDetail;

    @NameInMap("drive_log_detail")
    public DriveLogDetail driveLogDetail;

    @NameInMap("ent_mgmt_log_detail")
    public EntMgmtLogDetail entMgmtLogDetail;

    @NameInMap("file_log_detail")
    public FileLogDetail fileLogDetail;

    @NameInMap("group_log_detail")
    public GroupLogDetail groupLogDetail;

    @NameInMap("login_mgmt_log_detail")
    public LoginMgmtLogDetail loginMgmtLogDetail;

    @NameInMap("membership_log_detail")
    public MembershipLogDetail membershipLogDetail;

    @NameInMap("role_log_detail")
    public RoleLogDetail roleLogDetail;

    @NameInMap("security_log_detail")
    public SecurityLogDetail securityLogDetail;

    @NameInMap("share_link_log_detail")
    public ShareLinkLogDetail shareLinkLogDetail;

    @NameInMap("share_log_detail")
    public ShareLogDetail shareLogDetail;

    @NameInMap("user_log_detail")
    public UserLogDetail userLogDetail;

    public static LogDetail build(java.util.Map<String, ?> map) throws Exception {
        LogDetail self = new LogDetail();
        return TeaModel.build(map, self);
    }

    public LogDetail setAccountLogDetail(AccountLogDetail accountLogDetail) {
        this.accountLogDetail = accountLogDetail;
        return this;
    }
    public AccountLogDetail getAccountLogDetail() {
        return this.accountLogDetail;
    }

    public LogDetail setAuditMgmtLogDetail(AuditMgmtLogDetail auditMgmtLogDetail) {
        this.auditMgmtLogDetail = auditMgmtLogDetail;
        return this;
    }
    public AuditMgmtLogDetail getAuditMgmtLogDetail() {
        return this.auditMgmtLogDetail;
    }

    public LogDetail setDriveLogDetail(DriveLogDetail driveLogDetail) {
        this.driveLogDetail = driveLogDetail;
        return this;
    }
    public DriveLogDetail getDriveLogDetail() {
        return this.driveLogDetail;
    }

    public LogDetail setEntMgmtLogDetail(EntMgmtLogDetail entMgmtLogDetail) {
        this.entMgmtLogDetail = entMgmtLogDetail;
        return this;
    }
    public EntMgmtLogDetail getEntMgmtLogDetail() {
        return this.entMgmtLogDetail;
    }

    public LogDetail setFileLogDetail(FileLogDetail fileLogDetail) {
        this.fileLogDetail = fileLogDetail;
        return this;
    }
    public FileLogDetail getFileLogDetail() {
        return this.fileLogDetail;
    }

    public LogDetail setGroupLogDetail(GroupLogDetail groupLogDetail) {
        this.groupLogDetail = groupLogDetail;
        return this;
    }
    public GroupLogDetail getGroupLogDetail() {
        return this.groupLogDetail;
    }

    public LogDetail setLoginMgmtLogDetail(LoginMgmtLogDetail loginMgmtLogDetail) {
        this.loginMgmtLogDetail = loginMgmtLogDetail;
        return this;
    }
    public LoginMgmtLogDetail getLoginMgmtLogDetail() {
        return this.loginMgmtLogDetail;
    }

    public LogDetail setMembershipLogDetail(MembershipLogDetail membershipLogDetail) {
        this.membershipLogDetail = membershipLogDetail;
        return this;
    }
    public MembershipLogDetail getMembershipLogDetail() {
        return this.membershipLogDetail;
    }

    public LogDetail setRoleLogDetail(RoleLogDetail roleLogDetail) {
        this.roleLogDetail = roleLogDetail;
        return this;
    }
    public RoleLogDetail getRoleLogDetail() {
        return this.roleLogDetail;
    }

    public LogDetail setSecurityLogDetail(SecurityLogDetail securityLogDetail) {
        this.securityLogDetail = securityLogDetail;
        return this;
    }
    public SecurityLogDetail getSecurityLogDetail() {
        return this.securityLogDetail;
    }

    public LogDetail setShareLinkLogDetail(ShareLinkLogDetail shareLinkLogDetail) {
        this.shareLinkLogDetail = shareLinkLogDetail;
        return this;
    }
    public ShareLinkLogDetail getShareLinkLogDetail() {
        return this.shareLinkLogDetail;
    }

    public LogDetail setShareLogDetail(ShareLogDetail shareLogDetail) {
        this.shareLogDetail = shareLogDetail;
        return this;
    }
    public ShareLogDetail getShareLogDetail() {
        return this.shareLogDetail;
    }

    public LogDetail setUserLogDetail(UserLogDetail userLogDetail) {
        this.userLogDetail = userLogDetail;
        return this;
    }
    public UserLogDetail getUserLogDetail() {
        return this.userLogDetail;
    }

}
