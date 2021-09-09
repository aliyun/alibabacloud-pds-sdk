// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class LogDetail extends TeaModel {
    @NameInMap("drive_log_detail")
    public DriveLogDetail driveLogDetail;

    @NameInMap("file_log_detail")
    public FileLogDetail fileLogDetail;

    @NameInMap("group_log_detail")
    public GroupLogDetail groupLogDetail;

    @NameInMap("membership_log_detail")
    public MembershipLogDetail membershipLogDetail;

    @NameInMap("role_log_detail")
    public RoleLogDetail roleLogDetail;

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

    public LogDetail setDriveLogDetail(DriveLogDetail driveLogDetail) {
        this.driveLogDetail = driveLogDetail;
        return this;
    }
    public DriveLogDetail getDriveLogDetail() {
        return this.driveLogDetail;
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
