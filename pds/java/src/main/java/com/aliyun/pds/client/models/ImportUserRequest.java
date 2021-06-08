// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * Import user request
 */
public class ImportUserRequest extends TeaModel {
    @NameInMap("headers")
    public java.util.Map<String, String> headers;

    // 认证类型
    @NameInMap("authentication_type")
    @Validation(required = true)
    public String authenticationType;

    // 自动创建空间
    @NameInMap("auto_create_drive")
    public Boolean autoCreateDrive;

    // 是否能自己修改密码
    @NameInMap("deny_change_password_by_self")
    public Boolean denyChangePasswordBySelf;

    // 空间大小
    @NameInMap("drive_total_size")
    public Long driveTotalSize;

    // 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
    @NameInMap("extra")
    public String extra;

    // 唯一身份标识
    @NameInMap("identity")
    @Validation(required = true)
    public String identity;

    // 下次登录后是否强制修改密码
    @NameInMap("need_change_password_next_login")
    public Boolean needChangePasswordNextLogin;

    // 昵称
    @NameInMap("nick_name")
    @Validation(required = true)
    public String nickName;

    // 用户明文密码
    @NameInMap("plain_password")
    public String plainPassword;

    public static ImportUserRequest build(java.util.Map<String, ?> map) throws Exception {
        ImportUserRequest self = new ImportUserRequest();
        return TeaModel.build(map, self);
    }

    public ImportUserRequest setHeaders(java.util.Map<String, String> headers) {
        this.headers = headers;
        return this;
    }
    public java.util.Map<String, String> getHeaders() {
        return this.headers;
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

    public ImportUserRequest setPlainPassword(String plainPassword) {
        this.plainPassword = plainPassword;
        return this;
    }
    public String getPlainPassword() {
        return this.plainPassword;
    }

}
