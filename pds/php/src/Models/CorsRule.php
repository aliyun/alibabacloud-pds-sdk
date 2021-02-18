<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class CorsRule extends Model
{
    /**
     * @description AllowedHeader
     *
     * @example h*
     *
     * @var string[]
     */
    public $allowedHeader;

    /**
     * @description AllowedMethod
     *
     * @example PUT, GET
     *
     * @var string[]
     */
    public $allowedMethod;

    /**
     * @description AllowedOrigin
     *
     * @example *
     *
     * @var string[]
     */
    public $allowedOrigin;

    /**
     * @description ExposeHeader
     *
     * @example ETag
     *
     * @var string[]
     */
    public $exposeHeader;

    /**
     * @description MaxAgeSeconds
     *
     * @example 0
     *
     * @var int
     */
    public $maxAgeSeconds;
    protected $_name = [
        'allowedHeader' => 'allowed_header',
        'allowedMethod' => 'allowed_method',
        'allowedOrigin' => 'allowed_origin',
        'exposeHeader'  => 'expose_header',
        'maxAgeSeconds' => 'max_age_seconds',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->allowedHeader) {
            $res['allowed_header'] = $this->allowedHeader;
        }
        if (null !== $this->allowedMethod) {
            $res['allowed_method'] = $this->allowedMethod;
        }
        if (null !== $this->allowedOrigin) {
            $res['allowed_origin'] = $this->allowedOrigin;
        }
        if (null !== $this->exposeHeader) {
            $res['expose_header'] = $this->exposeHeader;
        }
        if (null !== $this->maxAgeSeconds) {
            $res['max_age_seconds'] = $this->maxAgeSeconds;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return CorsRule
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['allowed_header'])) {
            if (!empty($map['allowed_header'])) {
                $model->allowedHeader = $map['allowed_header'];
            }
        }
        if (isset($map['allowed_method'])) {
            if (!empty($map['allowed_method'])) {
                $model->allowedMethod = $map['allowed_method'];
            }
        }
        if (isset($map['allowed_origin'])) {
            if (!empty($map['allowed_origin'])) {
                $model->allowedOrigin = $map['allowed_origin'];
            }
        }
        if (isset($map['expose_header'])) {
            if (!empty($map['expose_header'])) {
                $model->exposeHeader = $map['expose_header'];
            }
        }
        if (isset($map['max_age_seconds'])) {
            $model->maxAgeSeconds = $map['max_age_seconds'];
        }

        return $model;
    }
}
