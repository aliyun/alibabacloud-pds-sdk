<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 获取download url response.
 */
class GetDownloadUrlResponse extends Model
{
    /**
     * @description expiration
     *
     * @example 2006-01-02T15:04:05.999Z07:00
     *
     * @var string
     */
    public $expiration;

    /**
     * @description method
     *
     * @example GET
     *
     * @var string
     */
    public $method;

    /**
     * @var RateLimit
     */
    public $ratelimit;

    /**
     * @description size
     *
     * @example 102400
     *
     * @var int
     */
    public $size;

    /**
     * @description streams url info
     *
     * @var mixed[]
     */
    public $streamsUrl;

    /**
     * @description url
     *
     * @example https://ccp.data.aliyuncs.com/hz22%2F5d79219b0aa9a7c995a94a96993ba3205cd91c5a%2F5d79219bf3261a5d38744da0834ed489b677a27a?Expires=xxxOSSAccessKeyId=xxx&Signature=xxx&response-content-disposition=attachment%3Bfilename%3DtBiZAoJPC2c8b13450eda4292b7f5f8010618e078.txt
     *
     * @var string
     */
    public $url;
    protected $_name = [
        'expiration' => 'expiration',
        'method'     => 'method',
        'ratelimit'  => 'ratelimit',
        'size'       => 'size',
        'streamsUrl' => 'streams_url',
        'url'        => 'url',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->expiration) {
            $res['expiration'] = $this->expiration;
        }
        if (null !== $this->method) {
            $res['method'] = $this->method;
        }
        if (null !== $this->ratelimit) {
            $res['ratelimit'] = null !== $this->ratelimit ? $this->ratelimit->toMap() : null;
        }
        if (null !== $this->size) {
            $res['size'] = $this->size;
        }
        if (null !== $this->streamsUrl) {
            $res['streams_url'] = $this->streamsUrl;
        }
        if (null !== $this->url) {
            $res['url'] = $this->url;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return GetDownloadUrlResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['expiration'])) {
            $model->expiration = $map['expiration'];
        }
        if (isset($map['method'])) {
            $model->method = $map['method'];
        }
        if (isset($map['ratelimit'])) {
            $model->ratelimit = RateLimit::fromMap($map['ratelimit']);
        }
        if (isset($map['size'])) {
            $model->size = $map['size'];
        }
        if (isset($map['streams_url'])) {
            $model->streamsUrl = $map['streams_url'];
        }
        if (isset($map['url'])) {
            $model->url = $map['url'];
        }

        return $model;
    }
}
