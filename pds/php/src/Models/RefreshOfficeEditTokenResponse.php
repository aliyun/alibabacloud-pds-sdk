<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 刷新office文档在线编辑凭证 response
 */
class RefreshOfficeEditTokenResponse extends Model {
    protected $_name = [
        'officeAccessToken' => 'office_access_token',
        'officeRefreshToken' => 'office_refresh_token',
    ];
    public function validate() {}
    public function toMap() {
        $res = [];
        if (null !== $this->officeAccessToken) {
            $res['office_access_token'] = $this->officeAccessToken;
        }
        if (null !== $this->officeRefreshToken) {
            $res['office_refresh_token'] = $this->officeRefreshToken;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return RefreshOfficeEditTokenResponse
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['office_access_token'])){
            $model->officeAccessToken = $map['office_access_token'];
        }
        if(isset($map['office_refresh_token'])){
            $model->officeRefreshToken = $map['office_refresh_token'];
        }
        return $model;
    }
    /**
     * @description AccessToken
     * @example ac80b70a70fe4c34914a12743ac3a6fbv2
     * @var string
     */
    public $officeAccessToken;

    /**
     * @description RefreshToken
     * @example ac80b70a70fe4c34914a12743ac3a6fbv2
     * @var string
     */
    public $officeRefreshToken;

}
