<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class ConfirmLinkRequest extends Model
{
    public $headers;

    /**
     * @description 待绑定的临时token，此token只能访问绑定、取消绑定接口
     *
     * @example ey***s=
     *
     * @var string
     */
    public $temporaryToken;
    protected $_name = [
        'temporaryToken' => 'temporary_token',
    ];

    public function validate()
    {
        Model::validateRequired('temporaryToken', $this->temporaryToken, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->temporaryToken) {
            $res['temporary_token'] = $this->temporaryToken;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return ConfirmLinkRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['headers'])) {
            $model->headers = $map['headers'];
        }
        if (isset($map['temporary_token'])) {
            $model->temporaryToken = $map['temporary_token'];
        }

        return $model;
    }
}
