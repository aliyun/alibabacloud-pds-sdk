<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 获取文档预览地址 response.
 */
class GetOfficePreviewUrlResponse extends Model
{
    /**
     * @description AccessToken
     *
     * @example ac80b70a70fe4c34914a12743ac3a6fbv2
     *
     * @var string
     */
    public $accessToken;

    /**
     * @description preview_url
     *
     * @example https://office-cn-shanghai.imm.aliyuncs.com/office/w/1023210024677934_a2_3899cdbd16b3061554556d9e949bb2fe85a944030bf147f8de1d79036f5e5a25?hidecmb=1&simple=1&_w_tokentype=1
     *
     * @var string
     */
    public $previewUrl;
    protected $_name = [
        'accessToken' => 'access_token',
        'previewUrl'  => 'preview_url',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->accessToken) {
            $res['access_token'] = $this->accessToken;
        }
        if (null !== $this->previewUrl) {
            $res['preview_url'] = $this->previewUrl;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return GetOfficePreviewUrlResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['access_token'])) {
            $model->accessToken = $map['access_token'];
        }
        if (isset($map['preview_url'])) {
            $model->previewUrl = $map['preview_url'];
        }

        return $model;
    }
}
