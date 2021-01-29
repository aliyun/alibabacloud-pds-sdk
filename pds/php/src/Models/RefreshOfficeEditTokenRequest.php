<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 刷新office文档在线编辑凭证
 */
class RefreshOfficeEditTokenRequest extends Model {
    protected $_name = [
        'additionData' => 'addition_data',
        'location' => 'location',
        'officeAccessToken' => 'office_access_token',
        'officeRefreshToken' => 'office_refresh_token',
    ];
    public function validate() {
        Model::validateRequired('officeAccessToken', $this->officeAccessToken, true);
        Model::validateRequired('officeRefreshToken', $this->officeRefreshToken, true);
    }
    public function toMap() {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->additionData) {
            $res['addition_data'] = $this->additionData;
        }
        if (null !== $this->location) {
            $res['location'] = $this->location;
        }
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
     * @return RefreshOfficeEditTokenRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['headers'])){
            $model->headers = $map['headers'];
        }
        if(isset($map['addition_data'])){
            $model->additionData = $map['addition_data'];
        }
        if(isset($map['location'])){
            $model->location = $map['location'];
        }
        if(isset($map['office_access_token'])){
            $model->officeAccessToken = $map['office_access_token'];
        }
        if(isset($map['office_refresh_token'])){
            $model->officeRefreshToken = $map['office_refresh_token'];
        }
        return $model;
    }
    public $headers;

    /**
     * @description addition_data
     * @var mixed[]
     */
    public $additionData;

    /**
     * @description location
     * @var string
     */
    public $location;

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
