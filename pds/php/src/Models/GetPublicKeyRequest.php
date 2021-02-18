<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class GetPublicKeyRequest extends Model
{
    public $headers;

    /**
     * @description App ID
     *
     * @example CNMrhxwPJHAReExa
     *
     * @var string
     */
    public $appId;
    protected $_name = [
        'appId' => 'app_id',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->appId) {
            $res['app_id'] = $this->appId;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return GetPublicKeyRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['headers'])) {
            $model->headers = $map['headers'];
        }
        if (isset($map['app_id'])) {
            $model->appId = $map['app_id'];
        }

        return $model;
    }
}
