<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 获取office文档在线编辑地址 response.
 */
class GetOfficeEditUrlResponse extends Model
{
    /**
     * @description EditUrl
     *
     * @example https://office-cn-shanghai.imm.aliyuncs.com/office/w/1023210024677934_a2_3899cdbd16b3061554556d9e949bb2fe85a944030bf147f8de1d79036f5e5a25?hidecmb=1&simple=1&_w_tokentype=1
     *
     * @var string
     */
    public $editUrl;

    /**
     * @description AccessToken
     *
     * @example ac80b70a70fe4c34914a12743ac3a6fbv2
     *
     * @var string
     */
    public $officeAccessToken;

    /**
     * @description RefreshToken
     *
     * @example ac80b70a70fe4c34914a12743ac3a6fbv2
     *
     * @var string
     */
    public $officeRefreshToken;
    protected $_name = [
        'editUrl'            => 'edit_url',
        'officeAccessToken'  => 'office_access_token',
        'officeRefreshToken' => 'office_refresh_token',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->editUrl) {
            $res['edit_url'] = $this->editUrl;
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
     *
     * @return GetOfficeEditUrlResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['edit_url'])) {
            $model->editUrl = $map['edit_url'];
        }
        if (isset($map['office_access_token'])) {
            $model->officeAccessToken = $map['office_access_token'];
        }
        if (isset($map['office_refresh_token'])) {
            $model->officeRefreshToken = $map['office_refresh_token'];
        }

        return $model;
    }
}
