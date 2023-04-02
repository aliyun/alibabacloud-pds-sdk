// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * # Import user request
 */
public class ImportUserRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    /**
     * <p>认证方式的显示名称</p>
     */
    @NameInMap("authentication_display_name")
    public String authenticationDisplayName;

    /**
     * <p>认证类型</p>
     */
    @NameInMap("authentication_type")
    @Validation(required = true)
    public String authenticationType;

    /**
     * <p>自动创建空间</p>
     */
    @NameInMap("auto_create_drive")
    public Boolean autoCreateDrive;

    @NameInMap("custom_identity")
    public String customIdentity;

    /**
     * <p>是否能自己修改密码</p>
     */
    @NameInMap("deny_change_password_by_self")
    public Boolean denyChangePasswordBySelf;

    /**
     * <p>空间大小</p>
     */
    @NameInMap("drive_total_size")
    public Long driveTotalSize;

    /**
     * <p>用户过期时间</p>
     */
    @NameInMap("expired_at")
    public Long expiredAt;

    /**
     * <p>额外的信息，比如type为mobile时，此字段为国家编号，不填默认86</p>
     */
    @NameInMap("extra")
    public String extra;

    /**
     * <p>唯一身份标识</p>
     */
    @NameInMap("identity")
    @Validation(required = true)
    public String identity;

    /**
     * <p>下次登录后是否强制修改密码</p>
     */
    @NameInMap("need_change_password_next_login")
    public Boolean needChangePasswordNextLogin;

    /**
     * <p>昵称</p>
     */
    @NameInMap("nick_name")
    @Validation(required = true)
    public String nickName;

    /**
     * <p>加入到group</p>
     */
    @NameInMap("parent_group_id")
    public String parentGroupId;

    /**
     * <p>用户明文密码</p>
     */
    @NameInMap("plain_password")
    public String plainPassword;

    public static ImportUserRequest build(java.util.Map<String, ?> map) throws Exception {
        ImportUserRequest self = new ImportUserRequest();
        return TeaModel.build(map, self);
    }

    public ImportUserRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public ImportUserRequest setAuthenticationDisplayName(String authenticationDisplayName) {
        this.authenticationDisplayName = authenticationDisplayName;
        return this;
    }
    public String getAuthenticationDisplayName() {
        return this.authenticationDisplayName;
    }

    public ImportUserRequest setAuthenticationType(String authenticationType) {
        this.authenticationType = authenticationType;
        return this;
    }
    public String getAuthenticationType() {
        return this.authenticationType;
    }

    public ImportUserRequest setAutoCreateDrive(Boolean autoCreateDrive) {
        this.autoCreateDrive = autoCreateDrive;
        return this;
    }
    public Boolean getAutoCreateDrive() {
        return this.autoCreateDrive;
    }

    public ImportUserRequest setCustomIdentity(String customIdentity) {
        this.customIdentity = customIdentity;
        return this;
    }
    public String getCustomIdentity() {
        return this.customIdentity;
    }

    public ImportUserRequest setDenyChangePasswordBySelf(Boolean denyChangePasswordBySelf) {
        this.denyChangePasswordBySelf = denyChangePasswordBySelf;
        return this;
    }
    public Boolean getDenyChangePasswordBySelf() {
        return this.denyChangePasswordBySelf;
    }

    public ImportUserRequest setDriveTotalSize(Long driveTotalSize) {
        this.driveTotalSize = driveTotalSize;
        return this;
    }
    public Long getDriveTotalSize() {
        return this.driveTotalSize;
    }

    public ImportUserRequest setExpiredAt(Long expiredAt) {
        this.expiredAt = expiredAt;
        return this;
    }
    public Long getExpiredAt() {
        return this.expiredAt;
    }

    public ImportUserRequest setExtra(String extra) {
        this.extra = extra;
        return this;
    }
    public String getExtra() {
        return this.extra;
    }

    public ImportUserRequest setIdentity(String identity) {
        this.identity = identity;
        return this;
    }
    public String getIdentity() {
        return this.identity;
    }

    public ImportUserRequest setNeedChangePasswordNextLogin(Boolean needChangePasswordNextLogin) {
        this.needChangePasswordNextLogin = needChangePasswordNextLogin;
        return this;
    }
    public Boolean getNeedChangePasswordNextLogin() {
        return this.needChangePasswordNextLogin;
    }

    public ImportUserRequest setNickName(String nickName) {
        this.nickName = nickName;
        return this;
    }
    public String getNickName() {
        return this.nickName;
    }

    public ImportUserRequest setParentGroupId(String parentGroupId) {
        this.parentGroupId = parentGroupId;
        return this;
    }
    public String getParentGroupId() {
        return this.parentGroupId;
    }

    public ImportUserRequest setPlainPassword(String plainPassword) {
        this.plainPassword = plainPassword;
        return this;
    }
    public String getPlainPassword() {
        return this.plainPassword;
    }

}
